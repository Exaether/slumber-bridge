from pydantic import BaseModel


class Range(BaseModel):
    direction: int
    grid: list[tuple[int]]
