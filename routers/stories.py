from fastapi import APIRouter, HTTPException
from pathlib import Path
import json

from core.data_store import data_store
from models.stories import StoryStageText, StoryBase, StoryDetail

router = APIRouter(prefix="/stories", tags=["stories"])

STORIES_BASE_PATH = Path(__file__).parent.parent / "data" / "stories"


@router.get("/", response_model=dict[str, StoryBase])
def get_stories():
    stories = {}
    for id, st in data_store.getStories().items():
        stories[id] = {}
        stories[id]["id"] = id
        stories[id]["title"] = st["title"]
        stories[id]["type"] = st["type"]
        stories[id]["startTime"] = st["startTime"]
        stories[id]["cover"] = st["cover"]
    return stories


@router.get("/{id}", response_model=StoryDetail)
def get_story(id: str):
    try:
        return data_store.getStory(id)
    except KeyError:
        raise HTTPException(status_code=404, detail="story not found")


@router.get("/{id}/{index}", response_model=StoryStageText)
def get_stage(id: str, index: int):
    try:
        stage = data_store.getStory(id)["stages"][index]
        stage_id = stage["id"]
        with open(STORIES_BASE_PATH / id / "stages" / (stage_id + ".json"), "r") as f:
            stage["text"] = json.load(f)
        return stage
    except KeyError:
        raise HTTPException(status_code=404, detail="story or stage not found")
