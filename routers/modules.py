from fastapi import APIRouter, HTTPException

from core.data_store import data_store
from models.mod import Module, ModulePhase


router = APIRouter(prefix="/modules", tags=["modules"])


@router.get("/", response_model=list[str])
def get_modules():
    return data_store.getModules().keys()


@router.get("/{id}", response_model=Module)
def get_module(id: str):
    try:
        return data_store.getModule(id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Module not found")


@router.get("/{id}/{level}", response_model=ModulePhase)
def get_module_level(id: str, level: int):
    try:
        if level > 0 and level <= 3:
            return data_store.getModule(id)["phases"][level - 1]
        else:
            raise HTTPException(status_code=404, detail="Module level not found")
    except KeyError:
        raise HTTPException(status_code=404, detail="Module not found")
