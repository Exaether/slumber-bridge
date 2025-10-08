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
    favorKeyFrames: list[int]


class Phase(BaseModel):
    id: int
    range: str
    maxLevel: int
    minStats: int
    maxStats: int


class AttributeKeyFrame(BaseModel):
    level: int
    maxHP: int
    atk: int
    defense: int = Field(..., alias="def")
    res: int
    cost: int
    aspd: int
    baseAttackTime: float
    respawnTime: int
    hpRecovery: int
    spRecovery: int
    maxDeployCount: int
    maxDeckStackCount: int
    tauntLevel: int
    baseForceLevel: int
