from fastapi import FastAPI
from routers import operators, ranges, skills

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(operators.router)
app.include_router(ranges.router)
app.include_router(skills.router)
