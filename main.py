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
    {"text": "How do I let our love die, When you're the only other keeper Of my most precious memories?", "author": "I'll Change for You"},
    {"text": "One morning, this sadness will fossilize and I will forget how to cry", "author": "Fireworks"},
    {"text": "As I got older, I learned I'm a drinker Sometimes, a drink feels like family", "author": "Bug Like an Angel"},
    {"text": "I need something bigger than the sky, Hold it in my arms and know it's mine", "author": "Remember My Name"}
]

# List of background images (Update this as you add all 10)
background_images = [
    "background.jpg",
    "background2.jpg",
    "background3.jpg",
    # Add the rest here...
]

@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_path = os.path.join(base_path, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/get-quote")
async def get_quote():
    # Pick a random quote and a random image
    quote = random.choice(quotes_data)
    bg_image = random.choice(background_images)
    
    # Return both as a single JSON object
    return {
        "text": quote["text"],
        "author": quote["author"],
        "background": f"/static/{bg_image}"
    }