from pydantic import BaseModel


class TalentCandidate(BaseModel):
    unlockPhase: int
    unlockPotentialRank: int
    description: str
    blackboard: dict[str, float]


class Talent(BaseModel):
    name: str
    token: str | None = None
    candidates: list[TalentCandidate]


class PotentialRank(BaseModel):
    type: str
    description: str
    attribute: str | None = None
    formula: str | None = None
    value: float | None = None


class TraitCandidate(BaseModel):
    unlockPhase: int
    overrideDescription: str | None = None
    blackboard: dict[str, float]


class Trait(BaseModel):
    description: str
    candidates: list[TraitCandidate]
