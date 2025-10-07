from pydantic import BaseModel


class Skill(BaseModel):
    id: str
    name: str
    skillType: str
    durationType: str
    spType: str
    levels: list[int]


class SkillLevel(BaseModel):
    description: str
    maxCharge: int
    spCost: int
    initSp: int
    duration: int
    blackboard: dict[str, float]
