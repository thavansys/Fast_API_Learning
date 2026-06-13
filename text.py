from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

@app.post("/text")
def receive_text(content: str = Body(..., media_type="text/plain")):
    return {
        "type": "Plain text",
        "content": content
    }