opsEN: list[str] = []
skillsEN: list[str] = []
modsEN: list[str] = []

skillsToken: dict[str, str] = {}
charEquip: dict[str, str] = {}
charSkins: dict[str, str] = {}


def parse_blackboard(blackboard):
    if type(blackboard) != list:
        return blackboard
    blackboard_data = {}
    for e in blackboard:
        blackboard_data[e["key"]] = e["value"]
    return blackboard_data


def parse_subProfDict(subProfDict):
    subProfNames = {}
    for key, data in subProfDict.items():
        subProfNames[key] = data["subProfessionName"]

    return subProfNames
