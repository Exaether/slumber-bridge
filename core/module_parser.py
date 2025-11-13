from pathlib import Path
import json

from core.common_parser import charEquip, parse_blackboard


mod_dir_path = Path(__file__).parent.parent / "data" / "modules"


def create_mod_json(id, mod):
    data = {}
    data["id"] = id
    data["phases"] = []
    for phase in mod["phases"]:
        phase_data = {}
        phase_data["parts"] = []
        for part in phase["parts"]:
            phase_data["parts"].append(parse_part(part))
        phase_data["attributes"] = parse_blackboard(phase["attributeBlackboard"])
        phase_data["tokenAttributes"] = {}
        for token, blackboard in phase["tokenAttributeBlackboard"].items():
            phase_data["tokenAttributes"][token] = parse_blackboard(blackboard)
        data["phases"].append(phase_data)

    json_str = json.dumps(data, indent=4)

    filename = id + ".json"

    with open(mod_dir_path / filename, "w") as f:
        f.write(json_str)


def parse_part(part):
    part_data = {}
    part_data["target"] = part["target"]
    part_data["isToken"] = part["isToken"]
    if (
        "candidates" in part["addOrOverrideTalentDataBundle"]
        and part["addOrOverrideTalentDataBundle"]["candidates"]
    ):
        part_data["talentCandidates"] = []
        for candidate in part["addOrOverrideTalentDataBundle"]["candidates"]:
            part_data["talentCandidates"].append(parse_mod_talent_candidate(candidate))

    if (
        "candidates" in part["overrideTraitDataBundle"]
        and part["overrideTraitDataBundle"]["candidates"]
    ):
        part_data["traitCandidates"] = []
        for candidate in part["overrideTraitDataBundle"]["candidates"]:
            part_data["traitCandidates"].append(parse_mod_trait_candidate(candidate))
    return part_data


def parse_mod_trait_candidate(candidate):
    candidate_data = {}
    candidate_data["unlockPhase"] = int(candidate["unlockCondition"]["phase"][-1])

    if "additionalDescription" in candidate:
        candidate_data["additionalDescription"] = candidate["additionalDescription"]
    if "overrideDescripton" in candidate:
        candidate_data["overrideDescription"] = candidate["overrideDescripton"]
    candidate_data["blackboard"] = parse_blackboard(candidate["blackboard"])
    return candidate_data


def parse_mod_talent_candidate(candidate):
    candidate_data = {}
    candidate_data["talentIndex"] = candidate["talentIndex"]
    candidate_data["description"] = candidate["upgradeDescription"]
    if "rangeId" in candidate:
        candidate_data["range"] = candidate["rangeId"]
    candidate_data["blackboard"] = parse_blackboard(candidate["blackboard"])
    return candidate_data
