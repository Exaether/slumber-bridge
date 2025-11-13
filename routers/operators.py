from fastapi import APIRouter, HTTPException

from core.data_store import data_store
from core.utils import calculate_level_keyFrame
from models.operator import (
    AttributeKeyFrame,
    Operator,
    OperatorBase,
    Phase,
)
from models.operators_extra import (
    PotentialRank,
    Talent,
    TalentCandidate,
    Trait,
    TraitCandidate,
)
from models.skill import Skill, SkillLevel

router = APIRouter(prefix="/operators", tags=["operators"])


@router.get("/", response_model=dict[str, OperatorBase])
def get_operators():
    ops = {}
    for id, op in data_store.getOperators().items():
        op = op["operator"]
        ops[id] = {}
        ops[id]["id"] = id
        ops[id]["name"] = op["name"]
        ops[id]["rarity"] = op["rarity"]
        ops[id]["profession"] = op["profession"]
        ops[id]["subProfession"] = op["subProfession"]
        if "nation" in op:
            ops[id]["nation"] = op["nation"]
        if "group" in op:
            ops[id]["group"] = op["group"]
    return ops


@router.get("/{id}", response_model=Operator)
def get_operator(id: str):
    try:
        return data_store.getOperator(id)["operator"]
    except KeyError:
        raise HTTPException(status_code=404, detail="Operator not found")


@router.get("/{id}/trait", response_model=Trait)
def get_trait(id: str):
    try:
        return data_store.getOperator(id)["trait"]
    except KeyError:
        raise HTTPException(status_code=404, detail="Operator not found")


@router.get("/{id}/trait/{phase}", response_model=TraitCandidate)
def get_trait_upgrade(id: str, phase: int):
    try:
        trait = data_store.getOperator(id)["trait"]
        for c in trait["candidates"]:
            if c["unlockPhase"] == phase:
                return c
        raise HTTPException(status_code=404, detail="Trait level not found")
    except KeyError:
        raise HTTPException(status_code=404, detail="Operator not found")


@router.get("/{id}/talents/{number}", response_model=Talent)
def get_talent(id: str, number: int):
    try:
        op = data_store.getOperator(id)
        if number in op["operator"]["talents"]:
            return op["talents"][number - 1]
        else:
            raise HTTPException(status_code=404, detail="Talent not found")
    except KeyError:
        raise HTTPException(status_code=404, detail="Operator not found")


@router.get("/{id}/talents/{number}/{phase}/{pot}", response_model=TalentCandidate)
def get_talent_candidate(id: str, number: int, phase: int, pot: int):
    try:
        op = data_store.getOperator(id)
        if number in op["operator"]["talents"]:
            tal = op["talents"][number - 1]
            for c in tal["candidates"]:
                if c["unlockPhase"] == phase and c["unlockPotentialRank"] == pot:
                    return c
            raise HTTPException(status_code=404, detail="Talent level not found")
        else:
            raise HTTPException(status_code=404, detail="Talent not found")
    except KeyError:
        raise HTTPException(status_code=404, detail="Operator not found")


@router.get("/{id}/potential/{rank}", response_model=PotentialRank)
def get_potential(id: str, rank: int):
    try:
        op = data_store.getOperator(id)
        if rank <= len(op["potentialRanks"]) and rank > 0:
            return op["potentialRanks"][rank - 1]
        else:
            raise HTTPException(status_code=404, detail="potential rank not found")
    except KeyError:
        raise HTTPException(status_code=404, detail="Operator not found")


@router.get("/{id}/phases/{number}", response_model=Phase)
def get_phase(id: str, number: int):
    try:
        op = data_store.getOperator(id)
        if number in op["operator"]["phases"]:
            return op["phases"][number]
        else:
            raise HTTPException(status_code=404, detail="phase not found")
    except KeyError:
        raise HTTPException(status_code=404, detail="Operator not found")


@router.get("/{id}/phases/{number}/stats/{level}", response_model=AttributeKeyFrame)
def get_stats(id: str, number: int, level: int):
    try:
        op = data_store.getOperator(id)
        if number in op["operator"]["phases"]:
            phase = op["phases"][number]
            if level == 1:
                return phase["minStats"]
            elif level == phase["maxLevel"]:
                return phase["maxStats"]
            elif level < phase["maxLevel"]:
                return calculate_level_keyFrame(phase, level)
            else:
                raise HTTPException(status_code=404, detail="Invalid level")
        else:
            raise HTTPException(status_code=404, detail="phase not found")
    except KeyError:
        raise HTTPException(status_code=404, detail="Operator not found")


@router.get("/{id}/favor", response_model=AttributeKeyFrame)
def get_favor_bonus(id: str):
    try:
        return data_store.getOperator(id)["favor"]
    except KeyError:
        raise HTTPException(status_code=404, detail="Operator not found")


@router.get("/{id}/skills/{number}", response_model=Skill, tags=["skills"])
def get_skill(id: str, number: int):
    try:
        op = data_store.getOperator(id)
        if number <= len(op["operator"]["skills"]) and number > 0:
            return data_store.getSkill(op["operator"]["skills"][number - 1])
        else:
            raise HTTPException(status_code=404, detail="Skill not found")
    except KeyError:
        raise HTTPException(status_code=404, detail="Operator not found")


@router.get("/{id}/skills/{number}/{level}", response_model=SkillLevel, tags=["skills"])
def get_skill_level(id: str, number: int, level: int):
    try:
        op = data_store.getOperator(id)
        if number <= len(op["operator"]["skills"]) and number > 0:
            skill = data_store.getSkill(op["operator"]["skills"][number - 1])
            if level <= len(skill["levels"]) and level > 0:
                return skill["levels"][level - 1]
            else:
                raise HTTPException(status_code=404, detail="Skill level not found")
        else:
            raise HTTPException(status_code=404, detail="Skill not found")
    except KeyError:
        raise HTTPException(status_code=404, detail="Operator not found")


@router.get("/{id}/skins", response_model=list[str])
def get_skins(id: str):
    try:
        return data_store.getOperator(id)["operator"]["skins"]
    except KeyError:
        raise HTTPException(status_code=404, detail="Operator not found")


@router.get("/{id}/full")
def get_full(id: str):
    try:
        return data_store.getOperator(id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Operator not found")
