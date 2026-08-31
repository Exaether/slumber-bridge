from pathlib import Path
import urllib.request
import os
import json
from core.common_parser import recordsNames, SOURCE, SOURCE_ALT
from typing import Any
import re
import shlex
from core.story_line_filters import param_map, commands_typos, useless_commands

story_dir_path = Path(__file__).parent.parent / "data" / "stories"
records_dir_path = Path(__file__).parent.parent / "data" / "records"

LINE_REGEX = re.compile(r"(?:\[([^]]+)\])?\s*(\S.*)?")
TAG_REGEX = re.compile(
    r'(\w+)(?:=((?:"[^"]+"|\'[^\']+\')))?(?:\(((?:[^"]|"[^"]*"|\'[^\']*\')*)\))?',
    re.IGNORECASE,
)

decision_state = ""


class UselessCommandException(Exception):
    def __init__(self):
        super().__init__()


def parse_value(string: str):
    if string.lower() == "true":
        return True
    if string.lower() == "false":
        return False

    try:
        return int(string)
    except ValueError:
        pass

    try:
        return float(string)
    except ValueError:
        pass

    return string


def parse_story_text(url) -> list[dict[str, Any]]:
    request = urllib.request.Request(url)

    with urllib.request.urlopen(request) as f:
        story_lines: list[dict[str, Any]] = []
        for line in f:
            line_dict: dict[str, Any] = {}
            line_match = LINE_REGEX.match(line.decode("utf-8").strip())
            if line_match:
                meta = line_match.group(1)
                text = line_match.group(2)
                if meta:
                    meta_match = TAG_REGEX.match(meta)
                    if meta_match:
                        command = meta_match.group(1).lower().strip()
                        value = meta_match.group(2)
                        params = meta_match.group(3)
                        line_dict["command"] = command
                        if value:
                            line_dict["value"] = value.strip("\"'")
                        if params:
                            params_dict = {}
                            # using shlex to handle commas inside strings
                            lexer = shlex.shlex(params, posix=True)
                            lexer.whitespace = ","
                            lexer.whitespace_split = True
                            for param in lexer:
                                try:
                                    key, val = param.split("=", 1)
                                    params_dict[key.strip()] = parse_value(
                                        val.strip())
                                except Exception:
                                    # fuck off if they can't format a file correctly
                                    # yes, there is like a single line where they used : instead of =
                                    pass
                                    # print('"', param, '"')
                            line_dict["params"] = params_dict
                if text:
                    line_dict["text"] = text
            story_lines.append(line_dict)
        return story_lines


def create_story_json(id, story, server):
    data = {}
    if story["actType"] == "NONE":
        retrieve_op_record(story, server)
        return
    data["id"] = id
    data["title"] = story["name"]
    data["type"] = story["actType"]
    data["startTime"] = story["startTime"]
    data["cover"] = story["storyEntryPicId"]
    data["stages"] = []

    # create the story dir
    if not os.path.exists(story_dir_path / id / "stages"):
        os.makedirs(story_dir_path / id / "stages")

    for s in story["infoUnlockDatas"]:
        stage = {}
        stage["index"] = s["storySort"]
        stage["code"] = s["storyCode"]
        stage["name"] = s["storyName"]
        stage["tag"] = s["avgTag"]
        stage["id"] = s["storyTxt"].split("/")[-1]
        data["stages"].append(stage)

        filename_json = stage["id"] + ".json"
        try:

            url = SOURCE + server + "/gamedata/story/" + s["storyTxt"] + ".txt"
            txt = update_story_text(parse_story_text(url))
            json_str = json.dumps(txt, indent=4)

            with open(story_dir_path / id / "stages" / filename_json, "w") as f:
                f.write(json_str)

        except urllib.error.HTTPError:
            # fix for 2 missing stories from ashleney repo
            url = SOURCE_ALT + "/story/" + s["storyTxt"] + ".txt"
            json_str = json.dumps(update_story_text(
                parse_story_text(url)), indent=4)

            with open(story_dir_path / id / "stages" / filename_json, "w") as f:
                f.write(json_str)

    json_str = json.dumps(data, indent=4)
    filename = id + ".json"

    with open(story_dir_path / id / filename, "w") as f:
        f.write(json_str)


def retrieve_op_record(story, server):
    stage = story["infoUnlockDatas"][0]
    id = stage["storyTxt"].split("/")[-1]
    stage_filename = id + ".txt"

    url = SOURCE + server + "/gamedata/story/obt/memory/" + stage_filename
    json_str = json.dumps(update_story_text(parse_story_text(url)), indent=4)
    filename_json = id + ".json"

    with open(story_dir_path.parent / "records" / filename_json, "w") as f:
        f.write(json_str)


def fix_line(line: dict[str, Any]):
    # fix params and commands typos and remove useless params
    global decision_state

    # command
    if "command" in line:
        if line["command"] in useless_commands:
            raise UselessCommandException()
        for command, typos in commands_typos.items():
            if line["command"] in typos:
                line["command"] = command

    # params
    if "params" in line:
        # text in params
        if "text" in line["params"]:
            line["text"] = line["params"]["text"]

        if "isblock" in line["params"]:
            line["params"]["block"] = line["params"]["isblock"]
            del line["params"]["isblock"]

        if line["command"] in param_map:
            result_params = {}
            for param, val in line["params"].items():
                for fix_param, typos in param_map[line["command"]].items():
                    if param in typos:
                        result_params[fix_param] = val
            line["params"] = result_params

    # specific fixes
    if "command" in line:
        match line["command"]:
            case "name":
                if "text" not in line:
                    raise UselessCommandException()
                if "value" not in line:
                    del line["command"]
            case "multiline":
                line["command"] = "name"
                if "params" in line and "name" in line["params"]:
                    line["value"] = line["params"]["name"]
                    del line["params"]
                else:
                    raise UselessCommandException()
            case "dialog" | "hidecgitem" | "hidehitem":
                if "params" in line:
                    del line["params"]
            case "theater":
                if "params" in line and "mode" in line["params"]:
                    line["value"] = line["params"]["mode"]
                    del line["params"]
                else:
                    raise UselessCommandException()
            case "video":
                if "params" in line and "res" in line["params"]:
                    line["value"] = line["params"]["res"]
                    del line["params"]
                else:
                    raise UselessCommandException()
            case "delay":
                if "params" in line and "time" in line["params"]:
                    line["value"] = line["params"]["time"]
                    del line["params"]
                else:
                    raise UselessCommandException()
            case "decision":
                line["params"]["values"] = str(line["params"]["values"])
                decision_state = line["params"]["values"]
            case "predicate":
                if "params" not in line:
                    line["params"] = {"references": decision_state}


def update_story_text(text: list[dict[str, Any]]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for line in text:
        try:
            fix_line(line)
        except UselessCommandException:
            continue
        result.append(line)
    return result
