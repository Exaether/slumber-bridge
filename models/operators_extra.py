from pydantic import BaseModel


class TalentCandidate(BaseModel):
    unlockPhase: int
    unlockPotentialRank: int
    description: str
    blackboard: dict[str, float]


class Talent(BaseModel):
    name: str
    candidates: list[TalentCandidate]


class PotentialRank(BaseModel):
    type: str
    description: str
    attribute: str | None
    formula: str | None
    value: float | None


class Trait(BaseModel):
    unlockPhase: int
    description: str
    blackboard: dict[str, float]
