from pyrogram import Client, filters
from pyrogram.types import Message
import json
import os

DB_FILE = "storage.json"

def load_commands():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def add_handlers(app: Client):

    @app.on_message(filters.regex(r"^/\w+") & filters.private)
    async def call_command(_, msg: Message):
        data = load_commands()
        cmd = msg.text.split()[0][1:].lower()
        if cmd in data:
            await msg.reply(data[cmd])