import json, os
from pyrogram import filters
from pyrogram.types import Message

DATA_PATH = "storage/data.json"

def load_data():
    if not os.path.exists(DATA_PATH):
        return {}
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)

def add_handlers(app):
    @app.on_message(filters.command("unpersonal"))
    async def delete_command(_, msg: Message):
        parts = msg.text.split()
        if len(parts) < 2:
            return await msg.reply("Format: `/unpersonal <trigger>`", quote=True)

        trigger = parts[1].lower()
        data = load_data()

        if trigger in data:
            del data[trigger]
            save_data(data)
            await msg.reply(f"Perintah `/{trigger}` dihapus!", quote=True)
        else:
            await msg.reply(f"Tidak ada perintah `/{trigger}` yang tersimpan.", quote=True)