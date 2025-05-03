from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# Basic
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Welcome to CRUD App"}

