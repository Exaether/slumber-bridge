from fastapi import APIRouter, HTTPException
from pathlib import Path

from core.data_store import data_store
from models.stories import RecordBase, RecordText

router = APIRouter(prefix="/records", tags=["stories"])

RECORDS_PATH = Path(__file__).parent.parent / "data" / "records"


@router.get("/", response_model=dict[str, RecordBase])
def get_records():
    recs = {}
    for id, name in data_store.getRecords().items():
        recs[id] = {}
        recs[id]["id"] = id
        recs[id]["name"] = name
    return recs


@router.get("/{id}", response_model=RecordText)
def get_record(id: str):
    try:
        rec = {}
        rec["id"] = id
        rec["name"] = data_store.getRecordName(id)

        with open(RECORDS_PATH / (id + ".txt"), "r") as f:
            rec["text"] = f.read()
        return rec
    except KeyError:
        raise HTTPException(status_code=404, detail="story or stage not found")
