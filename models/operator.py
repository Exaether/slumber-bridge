from pydantic import BaseModel, Field


class OperatorBase(BaseModel):
    id: str
    name: str
    rarity: int
    portrait: str
    profession: str
    subProfession: str
    nation: str
    group: str


class Operator(OperatorBase):
    displayNumber: str
    position: str
    tagList: list[str]
    skins: list[str]
    phases: list[int]
    skills: list[str]
    talents: list[int]


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
