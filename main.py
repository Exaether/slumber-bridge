from fastapi import FastAPI
from core.data_store import data_store
from core.parser import parse_all
from routers import operators, ranges, skills

app = FastAPI()

data_store.load_all()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/reload")
def read_root():
    data_store.load_all()
    return "reloaded"


@app.get("/fetch")
def read_root():
    parse_all()
    return "fetched data from kengxxiao"


app.include_router(operators.router)
app.include_router(ranges.router)
app.include_router(skills.router)
