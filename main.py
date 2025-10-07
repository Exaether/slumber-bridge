from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/operators")
def get_operators():
    return


@app.get("/operators/{id}")
def get_operator(id: str):
    return
