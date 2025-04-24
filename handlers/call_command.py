import json
import os
from pyrogram import Client, filters
from pyrogram.types import Message

DB_FILE = "personal_commands.json"

async def load_commands():
    if not os.path.exists(DB_FILE):
        return {}
    if os.path.getsize(DB_FILE) == 0:  # Cek kalau file kosong
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

async def save_commands(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f)

def add_handlers(app: Client):

    @app.on_message(filters.command("personal", ["/", "."]) & filters.text)
    async def save_command(client: Client, message: Message):
        parts = message.text.split(maxsplit=2)
        if len(parts) < 3:
            return await message.reply("Format: /personal <trigger> <reply>")

        trigger = parts[1].lower()
        response = parts[2]
        user_id = str(message.from_user.id)

        data = await load_commands()
        if user_id not in data:
            data[user_id] = {}
        data[user_id][trigger] = response
        await save_commands(data)

        await message.reply(f"Command /{trigger} saved!")

    @app.on_message(filters.command("unpersonal", ["/", "."]) & filters.text)
    async def delete_command(client: Client, message: Message):
        parts = message.text.split(maxsplit=1)
        if len(parts) < 2:
            return await message.reply("Format: /unpersonal <trigger>")

        trigger = parts[1].lower()
        user_id = str(message.from_user.id)

        data = await load_commands()
        if user_id in data and trigger in data[user_id]:
            del data[user_id][trigger]
            await save_commands(data)
            await message.reply(f"Command /{trigger} removed!")
        else:
            await message.reply(f"Command /{trigger} not found.")

    @app.on_message(filters.text & (filters.group | filters.private))
    async def handle_custom_command(client: Client, message: Message):
        if not message.text:
            return

        text = message.text.strip()
        if not (text.startswith("/") or text.startswith(".")):
            return

        trigger = text[1:].lower()
        user_id = str(message.from_user.id)

        data = await load_commands()
        if user_id in data and trigger in data[user_id]:
            await message.reply(data[user_id][trigger])