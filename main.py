from fastapi import FastAPI  ##     Simple FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
