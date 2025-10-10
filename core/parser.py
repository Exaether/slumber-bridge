from pathlib import Path
import urllib.request
import json

from skill_parser import create_skill_json
from operator_parser import create_op_json, parse_token

URL = {
    "character_table": "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/refs/heads/main/en_US/gamedata/excel/character_table.json",
    "skill_table": "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/refs/heads/main/en_US/gamedata/excel/skill_table.json",
    "range_table": "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/refs/heads/main/en_US/gamedata/excel/range_table.json",
}

DATA_DIR = Path(__file__).parent.parent / "data"


def get_operator_data():
    with urllib.request.urlopen(URL["character_table"]) as url:
        data = json.load(url)

    return data


def parse_operators():
    data = get_operator_data()

    for id, op in data.items():
        pro = op["profession"]
        match pro:
            case "TRAP":  # stage mechanics
                pass
            case "TOKEN":  # summons
                parse_token(id, op)
            case _:
                create_op_json(id, op)


def get_skill_data():
    with urllib.request.urlopen(URL["skill_table"]) as url:
        data = json.load(url)

    return data


def parse_skills():
    data = get_skill_data()

    for id, sk in data.items():
        create_skill_json(id, sk)


def retrieve_ranges():
    urllib.request.urlretrieve(URL["range_table"], DATA_DIR / "ranges.json")


if __name__ == "__main__":
    parse_operators()
    parse_skills()
    retrieve_ranges()
