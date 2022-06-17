from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
import os
import json
from pydantic import BaseModel
from typing import Optional, Literal
from fastapi.encoders import jsonable_encoder

app = FastAPI()

# Tutorial Model
class Tutorial(BaseModel):
    name: str
    difficulty: Literal["Easy", "Normal", "Difficult"]
    tutorial_id: Optional[str] = uuid4().hex


Tutorials_File = "tutorials.json"
Tutorial_Database = ["Scraper.py", "FastAPI.py", "Quiz_Game.py",  "Rock_Paper.py"]

if os.path.exists(Tutorials_File):
    with open(Tutorials_File, "r") as f:
        Tutorial_Database = json.load(f)

# /

@app.get("/")
async def home():
    return {"Message": "Welcome to my archive."}

# /list-tutorials

@app.get("/list-tutorials")
async def list_tutorials():
    return {"Tutorials": Tutorial_Database}

# /index

@app.get("/index/{index}")
async def index(index: int):
    if index < 0 or index >= len(Tutorial_Database):
        # Fail
        raise HTTPException(404, f"Index {index} is out of range {len(Tutorial_Database)}.")
    else:
        return {"Tutorial": Tutorial_Database[index]}

# /select-random select random tutorial

@app.get("/select-random")
async def select_random():
    return random.choice(Tutorial_Database)

# /add-tutorial

@app.post("/add-tutorial")
async def add_tutorial(tutorial: Tutorial):
    tutorial.tutorial_id = uuid4().hex
    json_tutorial = jsonable_encoder(tutorial)
    Tutorial_Database.append(json_tutorial)
    with open(Tutorials_File, "w") as f:
        json.dump(Tutorial_Database, f)

    return {"Message": f"Tutorial {tutorial} was added.", "tutorial_id": tutorial.tutorial_id}

# /get-tutorial?id=... 

@app.get("/get-tutorial")
async def get_tutorial(tutorial_id: str):
    for tutorial in Tutorial_Database:
        if tutorial["tutorial_id"] == tutorial_id:
            return tutorial
    raise HTTPException(404, f"Tutorial not found: {tutorial_id}")




