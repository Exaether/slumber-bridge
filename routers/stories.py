from fastapi import APIRouter, HTTPException
from pathlib import Path
import json
from typing import Any

from core.data_store import data_store
from core.story_line_filters import stripped_useless_commands
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
        stage = data_store.getStory(id)["stages"][index - 1]
        stage_id = stage["id"]
        with open(STORIES_BASE_PATH / id / "stages" / (stage_id + ".json"), "r") as f:
            stage["text"] = json.load(f)
        return stage
    except KeyError:
        raise HTTPException(status_code=404, detail="story or stage not found")


@router.get("/{id}/{index}/stripped", response_model=StoryStageText)
def get_stage_stripped(id: str, index: int):
    try:
        stage = data_store.getStory(id)["stages"][index - 1]
        stage_id = stage["id"]
        text: list[dict[str, Any]] = []
        with open(STORIES_BASE_PATH / id / "stages" / (stage_id + ".json"), "r") as f:
            text = json.load(f)
        stage["text"] = []
        for line in text:
            if (
                "command" not in line
                or line["command"] not in stripped_useless_commands
            ):
                stage["text"].append(line)
        return stage
    except KeyError:
        raise HTTPException(status_code=404, detail="story or stage not found")
