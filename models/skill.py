from pydantic import BaseModel


class Skill(BaseModel):
    id: str
    name: str
    skillType: str
    durationType: str
    spType: str
    token: str | None
    levels: list[int]


class SkillLevel(BaseModel):
    description: str
    range: str | None
    maxCharge: int
    spCost: int
    initSp: int
    duration: int
    blackboard: dict[str, float]
