from pathlib import Path
import json

from core.operator_parser import parse_phases, parse_talents, parse_trait


token_dir_path = Path(__file__).parent.parent / "data" / "tokens"


def create_token_json(id, token):
    # fixes
    if "talents" not in token:
        token["talents"] = []

    data = {}
    data["token"] = parse_token(id, token)
    data["phases"] = parse_phases(token["phases"])
    data["talents"] = parse_talents(token["talents"])
    data["trait"] = parse_trait(token)

    json_str = json.dumps(data, indent=4)

    filename = id + ".json"

    with open(token_dir_path / filename, "w") as f:
        f.write(json_str)


def parse_token(id, token):
    token_data = {}
    # base
    token_data["id"] = id
    token_data["name"] = token["name"]
    token_data["portait"] = ""  # TODO

    # details
    token_data["position"] = token["position"]
    token_data["phases"] = [i for i in range(len(token["phases"]))]
    token_data["skills"] = []
    for s in token["skills"]:
        if "skillId" in s:
            token_data["skills"].append(s["skillId"])
    if token["talents"]:
        token_data["talents"] = [i + 1 for i in range(len(token["talents"]))]
    else:
        token_data["talents"] = []

    return token_data
