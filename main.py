from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import random
import os

app = FastAPI()

base_path = os.path.dirname(os.path.abspath(__file__))

static_path = os.path.join(base_path, "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")


quotes_data = [
    {"text": "How do I let our love die, When you're the only other keeper Of my most precious memories?", "author": "I'll Change for You"},
    {"text": "One morning, this sadness will fossilize and I will forget how to cry", "author": "Fireworks"},
    {"text": "As I got older, I learned I'm a drinker Sometimes, a drink feels like family", "author": "Bug Like an Angel"},
    {"text": "I need something bigger than the sky, Hold it in my arms and know it's mine", "author": "Remember My Name"},
    {"text": "I'm not doing anything, My body's made of crushed little stars, And I'm not doing anything", "author": "My Body’s Made of Crushed Little Stars"},
    {"text": "Somebody kiss me, I'm going crazy,I'm walking 'round the house naked silver in the night", "author": "Blue Light"},
    {"text": "If I could, I'd be your little spoon and kiss your fingers forevermore", "author": "Your Best American Girl"},
    {"text": "And I don't blame you if you want to, Bury me in your memory, I'm not the girl I ought to be", "author": "Goodbye, My Danish Sweetheart"},
    {"text": "I don't need the world to see that I've been the best I can be, but I don't think I could stand to be where you don't see me", "author": "Francis Forever"},
    {"text": "I always wanted to die clean and pretty, But I'd be too busy on working days", "author": "Last Words of a Shooting Star"}
]


background_images = [
    "background.jpg",
    "background2.jpg",
    "background3.jpg",
    "background4.jpg",
    "background5.jpg",
    "background6.jpg"
]

@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_path = os.path.join(base_path, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/get-quote")
async def get_quote():
    quote = random.choice(quotes_data)
    bg_image = random.choice(background_images)
    
    return {
        "text": quote["text"],
        "author": quote["author"],
        "background": f"/static/{bg_image}"

    }


