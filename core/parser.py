from pathlib import Path
import urllib.request
import json

from core.common_parser import charEquip, charSkins, parse_subProfDict
from core.module_parser import create_mod_json
from core.token_parser import create_token_json
from core.skill_parser import create_skill_json
from core.operator_parser import create_op_json

SOURCE = "https://raw.githubusercontent.com/ArknightsAssets/ArknightsGamedata/refs/heads/master/en/gamedata/excel/"

DATA_DIR = Path(__file__).parent.parent / "data"


def get_data(table: str):
    table_url = SOURCE + table + ".json"
    with urllib.request.urlopen(table_url) as url:
        data = json.load(url)

    return data


def parse_skins():
    skins_data = get_data("skin_table")
    for id, skin in skins_data["charSkins"].items():
        if skin["charId"] not in charSkins:
            charSkins[skin["charId"]] = []
        if "portraitId" in skin:
            charSkins[skin["charId"]].append(skin["portraitId"])


def parse_uniequip():
    equips_data = get_data("uniequip_table")
    for char, equip in equips_data["charEquip"].items():
        charEquip[char] = equip[1::]

    subProfDict = parse_subProfDict(equips_data["subProfDict"])
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


def parse_modules():
    data = get_data("battle_equip_table")

    for id, mod in data.items():
        create_mod_json(id, mod)


def retrieve_ranges():
    urllib.request.urlretrieve(URL["range_table"], DATA_DIR / "ranges.json")


def parse_all():
    parse_skins()
    parse_uniequip()
    parse_modules()
    parse_operators()
    parse_skills()
    retrieve_ranges()


if __name__ == "__main__":
    parse_all()
