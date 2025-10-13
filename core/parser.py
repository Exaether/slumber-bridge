from pathlib import Path
import urllib.request
import json

import common_parser
from token_parser import create_token_json
from skill_parser import create_skill_json
from operator_parser import create_op_json

URL = {
    "character_table": "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/refs/heads/main/en_US/gamedata/excel/character_table.json",
    "skill_table": "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/refs/heads/main/en_US/gamedata/excel/skill_table.json",
    "range_table": "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/refs/heads/main/en_US/gamedata/excel/range_table.json",
    "uniequip_table": "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/refs/heads/main/en_US/gamedata/excel/uniequip_table.json",
}

DATA_DIR = Path(__file__).parent.parent / "data"


def get_data(table: str):
    with urllib.request.urlopen(URL[table]) as url:
        data = json.load(url)

    return data


def parse_uniequip():
    equips_data = get_data("uniequip_table")
    common_parser.charEquip = equips_data["charEquip"]

    subProfDict = common_parser.parse_subProfDict(equips_data["subProfDict"])
    with open(DATA_DIR / "subProfNames.json", "w") as f:
        f.write(json.dumps(subProfDict, indent=4))


def parse_operators():
    data = get_data("character_table")

    for id, op in data.items():
        pro = op["profession"]
        match pro:
            case "TRAP":  # stage mechanics
                pass
            case "TOKEN":  # summons
                create_token_json(id, op)
            case _:
                create_op_json(id, op)


def parse_skills():
    data = get_data("skill_table")

    for id, sk in data.items():
        create_skill_json(id, sk)


def retrieve_ranges():
    urllib.request.urlretrieve(URL["range_table"], DATA_DIR / "ranges.json")


if __name__ == "__main__":
    parse_uniequip()
    # parse_operators()
    # parse_skills()
    # retrieve_ranges()
