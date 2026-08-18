from pathlib import Path
import urllib.request
import os
import json
from core.common_parser import recordsNames, SOURCE, SOURCE_ALT
from typing import Any
import re
import ast
import shlex

story_dir_path = Path(__file__).parent.parent / "data" / "stories"

LINE_REGEX = re.compile(r"(?:\[([^]]+)\])?\s*(\S.*)?")
TAG_REGEX = re.compile(
    r'(\w+)(?:="([^"]+)")?(?:\(((?:[^"]|"[^"]*")*)\))?', re.IGNORECASE
)


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
                if text:
                    line_dict["text"] = text
                if meta:
                    meta_match = TAG_REGEX.match(meta)
                    if meta_match:
                        tag = meta_match.group(1).lower().strip()
                        value = meta_match.group(2)
                        params = meta_match.group(3)
                        line_dict["tag"] = tag
                        if value:
                            line_dict["value"] = value
                        if params:
                            # using shlex to handle commas inside strings
                            lexer = shlex.shlex(params, posix=True)
                            lexer.whitespace = ","
                            lexer.whitespace_split = True
                            for param in lexer:
                                try:
                                    key, val = param.split("=", 1)
                                    line_dict[key.strip()] = parse_value(
                                        val.strip())
                                except Exception:
                                    # fuck off if they can't format a file correctly
                                    # yes, there is like a single line where they used : instead of =
                                    pass
                                    # print('"', param, '"')
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
            txt = parse_story_text(url)
            json_str = json.dumps(txt, indent=4)

            with open(story_dir_path / id / "stages" / filename_json, "w") as f:
                f.write(json_str)

        except urllib.error.HTTPError:
            # fix for 2 missing stories from ashleney repo
            url = SOURCE_ALT + "/story/" + s["storyTxt"] + ".txt"
            json_str = json.dumps(parse_story_text(url), indent=4)

            with open(story_dir_path / id / "stages" / filename_json, "w") as f:
                f.write(json_str)

    json_str = json.dumps(data, indent=4)
    filename = id + ".json"

    with open(story_dir_path / id / filename, "w") as f:
        f.write(json_str)


def retrieve_op_record(story, server):
    stage = story["infoUnlockDatas"][0]
    id = stage["storyTxt"].split("/")[-1]
    recordsNames[id] = story["name"]
    stage_filename = id + ".txt"

    url = SOURCE + server + "/gamedata/story/obt/memory/" + stage_filename
    json_str = json.dumps(parse_story_text(url), indent=4)
    filename_json = id + ".json"

    with open(story_dir_path.parent / "records" / filename_json, "w") as f:
        f.write(json_str)


def create_records_names_json():
    json_str = json.dumps(recordsNames, indent=4)
    filename = "recordsNames.json"

    with open(story_dir_path.parent / "records" / filename, "w") as f:
        f.write(json_str)
