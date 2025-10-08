from ast import operator
import urllib.request
import json


def get_operator_data():
    with urllib.request.urlopen(
        "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/refs/heads/main/en_US/gamedata/excel/character_table.json"
    ) as url:
        data = json.load(url)

    return data


def parse_operators():
    data = get_operator_data()

    for id, op in data.items():
        pro = op["profession"]
        match pro:
            case "TRAP":
                pass
            case "TOKEN":
                parse_token(id, op)
            case _:
                parse_operator(id, op)


def parse_operator(id, op):
    data = {}
    # base
    data["id"] = id
    data["name"] = op["name"]
    data["rarity"] = int(op["rarity"][-1])
    data["portait"] = ""  # TODO
    data["profession"] = op["profession"]
    data["subProfession"] = op["subProfessionId"]
    data["nation"] = op["nationId"]
    data["group"] = op["groupId"]

    # details
    data["displayNumber"] = op["displayNumber"]
    data["position"] = op["position"]
    data["tagList"] = op["tagList"]
    data["skins"] = []  # TODO
    data["phases"] = [i for i in range(len(op["phases"]))]
    data["skills"] = [s["skillId"] for s in op["skills"]]
    if not op["talents"]:
        op["talents"] = []
    data["talents"] = [i + 1 for i in range(len(op["talents"]))]
    data["favorKeyFrames"] = [t["level"] for t in op["favorKeyFrames"]]

    json_data = json.dumps(data)
    print(json_data)
    print()


def parse_token(id, token):
    pass


if __name__ == "__main__":

    parse_operators()
