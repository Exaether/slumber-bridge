from fastapi import APIRouter

from models.skill import Skill, SkillLevel

router = APIRouter(prefix="/skills", tags=["skills"])


@router.get("/", response_model=list[str])
def get_skills():
    return


@router.get("/{id}", response_model=Skill)
def get_skill(id: str):
    return


@router.get("/{id}/{level}", response_model=SkillLevel)
def get_skill_level(id: str, level: int):
    return
