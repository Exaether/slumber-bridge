from pydantic import BaseModel


class Range(BaseModel):
    id: str
    direction: int
    grids: list[dict[str, int]]
