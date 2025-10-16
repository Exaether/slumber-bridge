from pydantic import BaseModel


class ModTraitCandidate(BaseModel):
    unlockPhase: int
    additionalDescription: str | None = None
    overrideDescription: str | None = None
    blackboard: dict[str, float]


class ModTalentCandidate(BaseModel):
    talentIndex: int
    description: str
    range: str | None = None
    blackboard: dict[str, float]


class ModulePart(BaseModel):
    target: str
    isToken: bool
    traitCandidates: list[ModTraitCandidate] | None = None
    talentCandidates: list[ModTalentCandidate] | None = None


class ModulePhase(BaseModel):
    parts: list[ModulePart]
    attributes: dict[str, float]
    tokenAttributes: dict[str, float]


class Module(BaseModel):
    id: str
    phases: list[ModulePhase]
