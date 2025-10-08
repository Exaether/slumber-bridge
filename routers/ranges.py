from fastapi import APIRouter

from models.range import Range

router = APIRouter(prefix="/ranges", tags=["ranges"])


@router.get("/", response_model=list[str])
def get_ranges():
    return


@router.get("/{id}", response_model=Range)
def get_range(id: str):
    return
