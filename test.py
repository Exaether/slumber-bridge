from pathlib import Path
from typing import Any
import json
from param_map import param_map

STORIES_PATH = Path(__file__).parent / "data" / "stories"

param_list = {}


def find_params(line: dict[str, Any]):
    for param in line:
        if param not in param_list:
            param_list[param] = 1
        else:
            param_list[param] += 1


def update_story_text(text: list[dict[str, Any]], title: str) -> list[dict[str, Any]]:
    result = []
    for line in text:
        result_line = {}
        if "tag" in line:
            result_line["tag"] = line["tag"]

            # remove useless params and fix typos
            if line["tag"] in param_map:
                for param_name, syn in param_map[line["tag"]].items():
                    for param in line:
                        if param in syn:
                            result_line[param_name] = line[param]

            if line["tag"] == "name":
                if "value" not in line:
                    print(title)
                    print(line)
                find_params(line)


if __name__ == "__main__":
    for file in (STORIES_PATH).glob("*/stages/*.json"):
        text = []
        with open(file, "r") as f:
            text = json.load(f)
        update_story_text(text, file.stem)
    print(param_list)
