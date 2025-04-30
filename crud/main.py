from fastapi import FastAPI

# Basic
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Welcome to CRUD App"}