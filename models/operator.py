from pydantic import BaseModel


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
    tagList: list[str]
    skins: list[str]
    phases: list[int]


class Phase(BaseModel):
    id: int
    range: str
    maxLevel: int
    minStats: int
    maxStats: int


class AttributeKeyFrame(BaseModel):
    level: int
    maxHP: int
    # ...
