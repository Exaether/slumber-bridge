from fastapi import FastAPI, Depends, HTTPException, Security
from core.data_store import data_store
from core.parser import parse_all
from routers import misc, modules, operators, skills
from fastapi.security.api_key import APIKeyHeader
import os

API_KEY = os.getenv("DATA_RELOAD_KEY")
API_KEY_NAME = "API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

app = FastAPI()

data_store.load_all()


async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return api_key


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/reload")
def load_files(api_key: str = Depends(verify_api_key)):
    data_store.load_all()
    return "Reloaded data"


@app.post("/update")
def parse_data(api_key: str = Depends(verify_api_key)):
    parse_all()
    data_store.load_all()
    return "Updated game data"


app.include_router(operators.router)
app.include_router(misc.router)
app.include_router(skills.router)
app.include_router(modules.router)
