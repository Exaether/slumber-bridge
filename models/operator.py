from pydantic import BaseModel, Field


class OperatorBase(BaseModel):
    id: str
    name: str
    rarity: int
    profession: str
    subProfession: str
    nation: str | None = None
    group: str | None = None


class Operator(OperatorBase):
    displayNumber: str
    position: str
    tagList: list[str]
    skins: list[str]
    phases: list[int]
    skills: list[str]
    talents: list[int]
    equips: list[str] | None = None


class AttributeKeyFrame(BaseModel):
    maxHP: int
    atk: int
    defense: int = Field(..., alias="def")
    res: int
    cost: int
    baseAttackTime: float
    respawnTime: int
    taunt: int


class Phase(BaseModel):
    range: str
    maxLevel: int
    minStats: AttributeKeyFrame
    maxStats: AttributeKeyFrame
