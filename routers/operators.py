from fastapi import APIRouter

from models.operator import AttributeKeyFrame, Operator, OperatorBase, Phase
from models.operators_extra import PotentialRank, Talent, TalentCandidate, Trait
from models.skill import Skill, SkillLevel

router = APIRouter(prefix="/operators", tags=["operators"])


@router.get("/", response_model=list[OperatorBase])
def get_operators():
    return


@router.get("/{id}", response_model=Operator)
def get_operator(id: str):
    return


@router.get("/{id}/trait", response_model=Trait)
def get_trait(id: str):
    return


@router.get("/{id}/trait/{phase}", response_model=Trait)
def get_trait_upgrade(id: str, phase: int):
    return


@router.get("/{id}/talents/{number}", response_model=Talent)
def get_talent(id: str, number: int):
    return


@router.get("/{id}/talents/{number}/{phase}/{pot}", response_model=TalentCandidate)
def get_talent_candidate(id: str, number: int, phase: int, pot: int):
    return


@router.get("/{id}/potential/{rank}", response_model=PotentialRank)
def get_potential(id: str, rank: int):
    return


@router.get("/{id}/phases/{number}", response_model=Phase)
def get_phase(id: str, number: int):
    return


@router.get("/{id}/phases/{number}/stats/{level}", response_model=AttributeKeyFrame)
def get_stats(id: str, number: int, level: int):
    return


@router.get("/{id}/favor}", response_model=AttributeKeyFrame)
def get_favor_bonus(id: str):
    return


@router.get("/{id}/skills/{number}", response_model=Skill, tags=["skills"])
def get_skill(id: str, number: int):
    return


@router.get("/{id}/skills/{number}/{level}", response_model=SkillLevel, tags=["skills"])
def get_skill_level(id: str, number: int, level: int):
    return
