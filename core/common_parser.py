SOURCE = "https://raw.githubusercontent.com/ArknightsAssets/ArknightsGamedata/refs/heads/master/"
SOURCE_ALT = "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData/5ba509ad5a07f17b7e220a25f1ff66794dd79af1/en_US/gamedata"
REPO_PATH = "/gamedata/excel/"

opsEN: list[str] = []
skillsEN: list[str] = []
modsEN: list[str] = []
storiesEN: list[str] = []

opsCN: list[str] = []
skillsCN: list[str] = []
modsCN: list[str] = []
storiesCN: list[str] = []

skillsToken: dict[str, str] = {}
charEquip: dict[str, str] = {}
charSkins: dict[str, str] = {}
recordsNames: dict[str, str] = {}


def parse_blackboard(blackboard):
    if blackboard is not list:
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
