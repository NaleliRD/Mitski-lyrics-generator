from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import random
import os

app = FastAPI()

# Absolute pathing ensures Vercel doesn't get "Lost"
base_path = os.path.dirname(os.path.abspath(__file__))

# Link the image folder
static_path = os.path.join(base_path, "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")


quotes_data = [
    {"text": "How do I let our love die When you're the only other keeper Of my most precious memories?", "author": "I'll Change for You"},
    {"text": "One morning, this sadness will fossilize And I will forget how to cry", "author": "Fireworks"},
    {"text": "As I got older, I learned I'm a drinker Sometimes, a drink feels like family": "Bug Like an Angel"},
    {"text": "I need something bigger than the sky Hold it in my arms and know it's mine", "author": "Remember My Name"}
]

@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_path = os.path.join(base_path, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/get-quote")
async def get_quote():
    return random.choice(quotes_data)