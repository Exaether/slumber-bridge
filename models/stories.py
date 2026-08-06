from pydantic import BaseModel, Field


class StoryStageBase(BaseModel):
    id: str
    index: int
    code: str
    name: str
    tag: str


class StoryStageText(StoryStageBase):
    text: str


class StoryBase(BaseModel):
    id: str
    title: str
    type: str
    startTime: int
    cover: str | None = None


class StoryDetail(StoryBase):
    stages: list[StoryStageBase]


class RecordBase(BaseModel):
    id: str
    name: str


class RecordText(RecordBase):
    text: str
