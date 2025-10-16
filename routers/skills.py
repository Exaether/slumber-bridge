from fastapi import APIRouter, HTTPException

from core.data_store import data_store
from models.skill import Skill, SkillLevel

router = APIRouter(prefix="/skills", tags=["skills"])


@router.get("/", response_model=list[str])
def get_skills():
    return data_store.getSkills().keys()


@router.get("/{id}", response_model=Skill)
def get_skill(id: str):
    try:
        return data_store.getSkill(id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Skill not found")


@router.get("/{id}/{level}", response_model=SkillLevel)
def get_skill_level(id: str, level: int):
    try:
        skill = data_store.getSkill(id)
        if level <= len(skill["levels"]) and level > 0:
            return skill["levels"][level - 1]
        else:
            raise HTTPException(status_code=404, detail="Skill level not found")
    except KeyError:
        raise HTTPException(status_code=404, detail="Skill not found")
