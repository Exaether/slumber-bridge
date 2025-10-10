from pathlib import Path
import json

from common_parser import parse_blackboard, skillsToken


op_dir_path = Path(__file__).parent.parent / "data" / "operators"


def create_op_json(id, op):
    # fixes
    if not op["talents"]:
        op["talents"] = []

    data = {}
    data["operator"] = parse_operator(id, op)
    data["phases"] = parse_phases(op["phases"])
    data["talents"] = parse_talents(op["talents"])
    data["potentialRanks"] = parse_potential(op["potentialRanks"])
    data["trait"] = parse_trait(op)
    data["favor"] = parse_attributesKeyFrame(op["favorKeyFrames"][1])

    json_str = json.dumps(data, indent=4)

    filename = id + ".json"

    with open(op_dir_path / filename, "w") as f:
        f.write(json_str)


def parse_operator(id, op):
    op_data = {}
    # base
    op_data["id"] = id
    op_data["name"] = op["name"]
    op_data["rarity"] = int(op["rarity"][-1])
    op_data["portait"] = ""  # TODO
    op_data["profession"] = op["profession"]
    op_data["subProfession"] = op["subProfessionId"]
    op_data["nation"] = op["nationId"]
    op_data["group"] = op["groupId"]

    # details
    op_data["displayNumber"] = op["displayNumber"]
    op_data["position"] = op["position"]
    op_data["tagList"] = op["tagList"]
    op_data["skins"] = []  # TODO
    op_data["phases"] = [i for i in range(len(op["phases"]))]
    op_data["skills"] = []
    for s in op["skills"]:
        op_data["skills"].append(s["skillId"])
        if s["overrideTokenKey"]:
            skillsToken[s["skillId"]] = s["overrideTokenKey"]
    op_data["talents"] = [i + 1 for i in range(len(op["talents"]))]

    return op_data


def parse_phases(phases):
    phases_data = []
    for p in phases:
        phase_data = {}
        phase_data["range"] = p["rangeId"]
        phase_data["maxLevel"] = p["maxLevel"]
        phase_data["minStats"] = parse_attributesKeyFrame(p["attributesKeyFrames"][0])
        phase_data["maxStats"] = parse_attributesKeyFrame(p["attributesKeyFrames"][1])
        phases_data.append(phase_data)

    return phases_data


def parse_attributesKeyFrame(keyFrame):
    keyFrame_data = {}
    keyFrame = keyFrame["data"]
    keyFrame_data["maxHP"] = keyFrame["maxHp"]
    keyFrame_data["atk"] = keyFrame["atk"]
    keyFrame_data["def"] = keyFrame["def"]
    keyFrame_data["res"] = keyFrame["magicResistance"]
    keyFrame_data["cost"] = keyFrame["cost"]
    keyFrame_data["baseAttackTime"] = keyFrame["baseAttackTime"]
    keyFrame_data["respawnTime"] = keyFrame["respawnTime"]
    keyFrame_data["taunt"] = keyFrame["tauntLevel"]
    return keyFrame_data


def parse_talents(talents):
    talents_data = []
    for t in talents:
        talent_data = {}
        talent_data["name"] = t["candidates"][0]["name"]
        if t["candidates"][0]["tokenKey"]:
            talent_data["token"] = t["candidates"][0]["tokenKey"]
        talent_data["candidates"] = [parse_talent_candidate(c) for c in t["candidates"]]
        talents_data.append(talent_data)

    return talents_data


def parse_talent_candidate(candidate):
    candidate_data = {}
    candidate_data["unlockPhase"] = int(candidate["unlockCondition"]["phase"][-1])
    candidate_data["unlockPotentialRank"] = candidate["requiredPotentialRank"]
    candidate_data["description"] = candidate["description"]
    candidate_data["blackboard"] = parse_blackboard(candidate["blackboard"])
    return candidate_data


def parse_potential(potentialRanks):
    potentialRanks_data = []
    for r in potentialRanks:
        rank_data = {}
        rank_data["type"] = r["type"]
        rank_data["description"] = r["description"]
        if r["type"] != "CUSTOM":
            buff = r["buff"]["attributes"]["attributeModifiers"][0]
            rank_data["attribute"] = buff["attributeType"]
            rank_data["formula"] = buff["formulaItem"]
            rank_data["value"] = buff["value"]
        potentialRanks_data.append(rank_data)

    return potentialRanks_data


def parse_trait(op):
    trait_data = {}
    trait_data["description"] = op["description"]
    candidates_data = []
    if op["trait"]:
        for c in op["trait"]["candidates"]:
            candidate_data = {}
            candidate_data["UnlockPhase"] = int(c["unlockCondition"]["phase"][-1])
            candidate_data["overrideDescription"] = c["overrideDescripton"]
            candidate_data["blackboard"] = parse_blackboard(c["blackboard"])
            candidates_data.append(candidate_data)
    trait_data["candidates"] = candidates_data
    return trait_data


def parse_token(id, token):
    pass
