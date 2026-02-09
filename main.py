from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import random
import os

app = FastAPI()

# Absolute pathing ensures Vercel doesn't get "Lost"
base_path = os.path.dirname(os.path.abspath(__file__))

# Link the image folder
app.mount("/static", StaticFiles(directory=base_path), name="static")

quotes_data = [
    {"text": "Man, this week has been tough, been sayin' that for a year", "author": "Little Simz"},
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Stay hungry, stay foolish.", "author": "Steve Jobs"},
    {"text": "Everything you've ever wanted is on the other side of fear.", "author": "George Addair"}
]

@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_path = os.path.join(base_path, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/get-quote")
async def get_quote():
    return random.choice(quotes_data)