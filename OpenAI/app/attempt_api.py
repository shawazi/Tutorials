from fastapi import FastAPI, HTTPException
from attempt import MAX_INPUT_LENGTH, generate_tangents, generate_keywords
from mangun import Mangum

app = FastAPI()
handler = Mangum(app)
MAX_INPUT_LENGTH = 32


@app.get("/generate_tangents")
async def generate_tangents_api(prompt: str):
    validate_input_length(prompt)
    tangents = generate_tangents(prompt)
    return {"tangents": tangents, "keywords": []}


@app.get("/generate_keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    keywords = generate_keywords(prompt)
    return {"tangents": None, "keywords": keywords}

@app.get("/generate_tangents_and_keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    tangents = generate_tangents(prompt)
    keywords = generate_keywords(prompt)
    return {"tangents": tangents, "keywords": keywords}

def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(status_code = 400, detail = f"Input length is too long. Must be under {MAX_INPUT_LENGTH} characters.")

# uvicorn attempt_api:app --reload

# http://127.0.0.1:8000