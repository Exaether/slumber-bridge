from pathlib import Path
import urllib.request
import json

from core.common_parser import (
    charEquip,
    charSkins,
    modsEN,
    opsEN,
    skillsEN,
    storiesEN,
    modsCN,
    opsCN,
    skillsCN,
    storiesCN,
    parse_subProfDict,
    recordsNames,
    REPO_PATH,
    SOURCE,
)
from core.module_parser import create_mod_json
from core.token_parser import create_token_json
from core.skill_parser import create_skill_json
from core.operator_parser import create_op_json
from core.story_parser import create_story_json

DATA_DIR = Path(__file__).parent.parent / "data"


def get_data(table: str, server: str):
    table_url = SOURCE + server + REPO_PATH + table + ".json"
    with urllib.request.urlopen(table_url) as url:
        data = json.load(url)

    return data


def parse_skins():
    skins_data = get_data("skin_table", "cn")
    for id, skin in skins_data["charSkins"].items():
        if skin["charId"] not in charSkins:
            charSkins[skin["charId"]] = []
        if "portraitId" in skin:
            charSkins[skin["charId"]].append(skin["portraitId"])


def parse_uniequip():
    equips_data = get_data("uniequip_table", "cn")
    for char, equip in equips_data["charEquip"].items():
        charEquip[char] = equip[1::]

    subProfDict = parse_subProfDict(equips_data["subProfDict"])
    with open(DATA_DIR / "subProfNames.json", "w") as f:
        f.write(json.dumps(subProfDict, indent=4))


def parse_operators():
    # load already parsed ops
    with open(DATA_DIR / "opsEN.json", "r") as f:
        opsEN = json.load(f)
    with open(DATA_DIR / "opsCN.json", "r") as f:
        opsCN = json.load(f)

    data = get_data("character_table", "en")

    for id, op in data.items():
        if id not in opsEN:
            pro = op["profession"]
            match pro:
                case "TRAP":  # stage mechanics
                    pass
                case "TOKEN":  # summons
                    create_token_json(id, op)
                case _:
                    create_op_json(id, op)
            opsEN.append(id)

    with open(DATA_DIR / "opsEN.json", "w") as f:
        f.write(json.dumps(opsEN, indent=4))

    # CN ops
    data = get_data("character_table", "cn")

    for id, op in data.items():
        if id not in opsEN and id not in opsCN:
            pro = op["profession"]
            match pro:
                case "TRAP":  # stage mechanics
                    pass
                case "TOKEN":  # summons
                    create_token_json(id, op)
                case _:
                    create_op_json(id, op)
            opsCN.append(id)

    with open(DATA_DIR / "opsCN.json", "w") as f:
        f.write(json.dumps(opsCN, indent=4))


def parse_skills():
    # load already parsed skill
    with open(DATA_DIR / "skillsEN.json", "r") as f:
        skillsEN = json.load(f)
    with open(DATA_DIR / "skillsCN.json", "r") as f:
        skillsCN = json.load(f)

    data = get_data("skill_table", "en")

    for id, sk in data.items():
        if id not in skillsEN:
            create_skill_json(id, sk)
            skillsEN.append(id)

    with open(DATA_DIR / "skillsEN.json", "w") as f:
        f.write(json.dumps(skillsEN, indent=4))

    # CN skills
    data = get_data("skill_table", "cn")

    for id, sk in data.items():
        if id not in skillsEN and id not in skillsCN:
            create_skill_json(id, sk)
            skillsCN.append(id)

    with open(DATA_DIR / "skillsCN.json", "w") as f:
        f.write(json.dumps(skillsCN, indent=4))


def parse_modules():
    # load already parsed mods
    with open(DATA_DIR / "modsEN.json", "r") as f:
        modsEN = json.load(f)
    with open(DATA_DIR / "modsCN.json", "r") as f:
        modsCN = json.load(f)

    data = get_data("battle_equip_table", "en")

    for id, mod in data.items():
        if id not in modsEN:
            create_mod_json(id, mod)
            modsEN.append(id)

    with open(DATA_DIR / "modsEN.json", "w") as f:
        f.write(json.dumps(modsEN, indent=4))

    # CN mods
    data = get_data("battle_equip_table", "cn")

    for id, mod in data.items():
        if id not in modsEN and id not in modsCN:
            create_mod_json(id, mod)
            modsCN.append(id)

    with open(DATA_DIR / "modsCN.json", "w") as f:
        f.write(json.dumps(modsCN, indent=4))


def retrieve_ranges():
    urllib.request.urlretrieve(
        SOURCE + "cn" + REPO_PATH + "range_table.json", DATA_DIR / "ranges.json"
    )


def parse_stories():
    # load already downloaded stories
    global storiesEN
    with open(DATA_DIR / "storiesEN.json", "r") as f:
        storiesEN = json.load(f)
    global storiesCN
    with open(DATA_DIR / "storiesCN.json", "r") as f:
        storiesCN = json.load(f)
    global recordsNames
    with open(DATA_DIR / "records" / "recordsNames.json", "r") as f:
        recordsNames = json.load(f)

    data = get_data("story_review_table", "en")

    for id, story in data.items():
        if story["actType"] == "NONE":
            recordsNames[id] = story["name"]
        if id not in storiesEN:
            create_story_json(id, story, "en")
            storiesEN.append(id)
            with open(DATA_DIR / "storiesEN.json", "w") as f:
                f.write(json.dumps(storiesEN, indent=4))

    # CN stories
    data = get_data("story_review_table", "cn")

    for id, story in data.items():
        if story["actType"] == "NONE" and id not in storiesEN:
            recordsNames[id] = story["name"]
        if id not in storiesEN and id not in storiesCN:
            create_story_json(id, story, "cn")
            storiesCN.append(id)
            with open(DATA_DIR / "storiesCN.json", "w") as f:
                f.write(json.dumps(storiesCN, indent=4))

    json_str = json.dumps(recordsNames, indent=4)
    filename = "recordsNames.json"

    with open(DATA_DIR / "records" / filename, "w") as f:
        f.write(json_str)


def parse_all():
    parse_skins()
    # links between ops and mods
    parse_uniequip()
    parse_modules()
    parse_operators()
    parse_skills()
    retrieve_ranges()
    parse_stories()


if __name__ == "__main__":
    parse_all()
