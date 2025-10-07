from pydantic import BaseModel


class range(BaseModel):
    direction: int
    grid: list[tuple[int]]
