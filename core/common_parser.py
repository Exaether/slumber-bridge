skillsToken = {}
charEquip = {}


def parse_blackboard(blackboard):
    blackboard_data = {}
    for e in blackboard:
        blackboard_data[e["key"]] = e["value"]
    return blackboard_data


def parse_subProfDict(subProfDict):
    subProfNames = {}
    for key, data in subProfDict.items():
        subProfNames[key] = data["subProfessionName"]

    return subProfNames
