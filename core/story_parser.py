from pathlib import Path
import urllib.request
import os
import json
from core.common_parser import recordsNames, SOURCE, SOURCE_ALT, downloadedENStories

story_dir_path = Path(__file__).parent.parent / "data" / "stories"


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
    if not os.path.exists(story_dir_path / id):
        os.makedirs(story_dir_path / id)

    for s in story["infoUnlockDatas"]:
        stage = {}
        stage["index"] = s["storySort"]
        stage["code"] = s["storyCode"]
        stage["name"] = s["storyName"]
        stage["tag"] = s["avgTag"]
        stage["id"] = s["storyTxt"].split("/")[-1]
        data["stages"].append(stage)

        stage_filename = stage["id"] + ".txt"
        if stage["id"] not in downloadedENStories:
            try:
                urllib.request.urlretrieve(
                    SOURCE + server + "/gamedata/story/" + s["storyTxt"] + ".txt",
                    story_dir_path / id / stage_filename,
                )
            except:
                # fix for 2 missing stories from ashleney repo
                urllib.request.urlretrieve(
                    SOURCE_ALT + "/story/" + s["storyTxt"] + ".txt",
                    story_dir_path / id / stage_filename,
                )
            if server == "en":
                downloadedENStories.append(stage["id"])

    json_str = json.dumps(data, indent=4)
    filename = id + ".json"

    with open(story_dir_path / id / filename, "w") as f:
        f.write(json_str)


def retrieve_op_record(story, server):
    stage = story["infoUnlockDatas"][0]
    id = stage["storyTxt"].split("/")[-1]
    recordsNames[id] = story["name"]
    stage_filename = id + ".txt"
    if id not in downloadedENStories:
        urllib.request.urlretrieve(
            SOURCE + server + "/gamedata/story/obt/memory/" + stage_filename,
            story_dir_path.parent / "records" / stage_filename,
        )
        if server == "en":
            downloadedENStories.append(id)


def create_records_names_json():
    json_str = json.dumps(recordsNames, indent=4)
    filename = "recordsNames.json"

    with open(story_dir_path.parent / "records" / filename, "w") as f:
        f.write(json_str)


def load_downloaded_stories_list():
    with open(story_dir_path / "downloadedENStories.json") as f:
        downloadedENStories = json.load(f)


def write_downloaded_stories_list():
    json_str = json.dumps(downloadedENStories, indent=4)
    filename = "downloadedENStories.json"

    with open(story_dir_path / filename, "w") as f:
        f.write(json_str)
