from pathlib import Path
import json

from common_parser import parse_blackboard, skillsToken

sk_dir_path = Path(__file__).parent.parent / "data" / "skills"


def create_skill_json(id, sk):
    data = parse_skill(id, sk)

    json_str = json.dumps(data, indent=4)

    filename = id + ".json"

    with open(sk_dir_path / filename, "w") as f:
        f.write(json_str)


def parse_skill(id, sk):
    sk_data = {}

    skLevel = sk["levels"][0]
    sk_data["id"] = id
    sk_data["name"] = skLevel["name"]
    sk_data["skillType"] = skLevel["skillType"]
    sk_data["durationType"] = skLevel["durationType"]
    sk_data["spType"] = skLevel["spData"]["spType"]
    if id in skillsToken.keys():
        sk_data["token"] = skillsToken[id]
    sk_data["levels"] = [parse_skill_level(l) for l in sk["levels"]]

    return sk_data


def parse_skill_level(level):
    level_data = {}

    level_data["description"] = level["description"]
    if level["rangeId"]:
        level_data["range"] = level["rangeId"]
    level_data["maxCharge"] = level["spData"]["maxChargeTime"]
    level_data["spCost"] = level["spData"]["spCost"]
    level_data["initSp"] = level["spData"]["initSp"]
    level_data["duration"] = level["duration"]
    level_data["blackboard"] = parse_blackboard(level["blackboard"])

    return level_data
