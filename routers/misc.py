from fastapi import APIRouter

from core.data_store import data_store
from models.range import Range

router = APIRouter()


@router.get("/ranges/", response_model=dict[str, Range], tags=["ranges"])
def get_ranges():
    return data_store.getRanges()


@router.get("/ranges/{id}", response_model=Range, tags=["ranges"])
def get_range(id: str):
    return data_store.getRange(id)


@router.get("/subProfNames", response_model=dict[str, str])
def get_subProfNames():
    return data_store.getSubProfNames()


@router.get("/subProfNames/{id}", response_model=str)
def get_subProfName(id: str):
    return data_store.getSubProfName(id)
