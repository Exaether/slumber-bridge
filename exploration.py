from pathlib import Path
from typing import Any
import json

STORIES_PATH = Path(__file__).parent / "data" / "stories"
RECORDS_PATH = Path(__file__).parent / "data" / "records"

param_list: dict[str, int] = {}
tag_cnt = 0
val_cnt = 0
text_cnt = 0

decision_state = ""


def find_params(line: dict[str, Any]):
    for param in line["params"]:
        if param not in param_list:
            param_list[param] = 1
        else:
            param_list[param] += 1


def story_search(text: list[dict[str, Any]], title: str, tag: str):
    for line in text:
        if "command" in line:

            if line["command"] == tag:
                if "" in line:
                    print(line)
                global tag_cnt
                tag_cnt += 1
                if "value" in line:
                    global val_cnt
                    val_cnt += 1
                if "text" in line:
                    global text_cnt
                    text_cnt += 1
                if "params" in line:
                    find_params(line)


if __name__ == "__main__":

    tag = "effect"

    for file in (STORIES_PATH).glob("*/stages/*.json"):
        text = []
        with open(file, "r") as f:
            text = json.load(f)
        story_search(text, file.stem, tag)

    for file in (RECORDS_PATH).glob("*.json"):
        if file.stem == "recordsNames":
            continue
        text = []
        with open(file, "r") as f:
            text = json.load(f)
        story_search(text, file.stem, tag)
    print("tag: ", tag)
    print("count: ", tag_cnt)
    print("values count: ", val_cnt)
    print("text count: ", text_cnt)
    print("params: ", param_list)
