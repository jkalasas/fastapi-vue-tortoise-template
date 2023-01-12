from fastapi import FastAPI

app = FastAPI(title="Template API")


@app.get("/")
def index():
    return {"hello": "world"}
