import json, os
from pyrogram import filters
from pyrogram.types import Message

DATA_PATH = "storage/data.json"

def load_data():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def add_handlers(app):
    @app.on_message(filters.regex(r"^/\w+"))
    async def call_command(_, msg: Message):
        text = msg.text or ""
        trigger = text.split()[0][1:].lower()
        data = load_data()

        if trigger in data:
            await msg.reply(data[trigger], quote=True)