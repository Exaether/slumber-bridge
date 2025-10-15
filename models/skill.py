from pydantic import BaseModel


class SkillLevel(BaseModel):
    description: str
    range: str | None = None
    maxCharge: int
    spCost: int
    initSp: int
    duration: int
    blackboard: dict[str, float]


class Skill(BaseModel):
    id: str
    name: str
    skillType: str
    durationType: str
    spType: str
    token: str | None = None
    levels: list[SkillLevel]
