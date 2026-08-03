from pathlib import Path
import urllib.request
import json

from core.common_parser import (
    charEquip,
    charSkins,
    modsEN,
    opsEN,
    parse_subProfDict,
    skillsEN,
    storiesEN,
    downloadedENStories,
    REPO_PATH,
    SOURCE,
)
from core.module_parser import create_mod_json
from core.token_parser import create_token_json
from core.skill_parser import create_skill_json
from core.operator_parser import create_op_json
from core.story_parser import (
    create_story_json,
    create_records_names_json,
    load_downloaded_stories_list,
    write_downloaded_stories_list,
)

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
    data = get_data("character_table", "en")

    for id, op in data.items():
        opsEN.append(id)
        pro = op["profession"]
        match pro:
            case "TRAP":  # stage mechanics
                pass
            case "TOKEN":  # summons
                create_token_json(id, op)
            case _:
                create_op_json(id, op)

    data = get_data("character_table", "cn")

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


def parse_skills():
    data = get_data("skill_table", "en")

    for id, sk in data.items():
        skillsEN.append(id)
        create_skill_json(id, sk)

    data = get_data("skill_table", "cn")

    for id, sk in data.items():
        if id not in skillsEN:
            create_skill_json(id, sk)


def parse_modules():
    data = get_data("battle_equip_table", "en")

    for id, mod in data.items():
        modsEN.append(id)
        create_mod_json(id, mod)

    data = get_data("battle_equip_table", "cn")

    for id, mod in data.items():
        if id not in modsEN:
            create_mod_json(id, mod)


def retrieve_ranges():
    urllib.request.urlretrieve(
        SOURCE + "cn" + REPO_PATH + "range_table.json", DATA_DIR / "ranges.json"
    )


def parse_stories():
    load_downloaded_stories_list()

    data = get_data("story_review_table", "en")

    for id, story in data.items():
        storiesEN.append(id)
        create_story_json(id, story, "en")

    data = get_data("story_review_table", "cn")

    for id, story in data.items():
        if id not in storiesEN:
            create_story_json(id, story, "cn")

    create_records_names_json()
    write_downloaded_stories_list()


def parse_all():
    parse_skins()
    parse_uniequip()
    parse_modules()
    parse_operators()
    parse_skills()
    retrieve_ranges()
    parse_stories()


if __name__ == "__main__":
    parse_all()
