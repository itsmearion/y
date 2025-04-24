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
    @app.on_message(filters.command("personal"))
    async def save_command(_, msg: Message):
        parts = msg.text.split(maxsplit=2)
        if len(parts) < 2:
            return await msg.reply("Format: `/personal <trigger> [text]`", quote=True)

        trigger = parts[1].lower()
        reply_text = parts[2] if len(parts) > 2 else msg.reply_to_message.text if msg.reply_to_message else None

        if not reply_text:
            return await msg.reply("Tidak ada teks untuk disimpan.", quote=True)

        data = load_data()
        data[trigger] = reply_text
        save_data(data)
        await msg.reply(f"Perintah `/{trigger}` disimpan!", quote=True)