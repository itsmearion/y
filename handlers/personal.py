from pyrogram import Client, filters
from pyrogram.types import Message
import json, os

DB_FILE = "storage.json"

def load_commands():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_commands(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_handlers(app: Client):

    @app.on_message(filters.command("personal") & filters.private)
    async def save_command(_, msg: Message):
        data = load_commands()

        if msg.reply_to_message:
            parts = msg.text.split()
            if len(parts) >= 2:
                key = parts[1].lower()
                data[key] = msg.reply_to_message.text or msg.reply_to_message.caption
                save_commands(data)
                await msg.reply(f"Command /{key} saved from reply!")
            else:
                await msg.reply("Gunakan /personal <command> sebagai reply.")

        else:
            parts = msg.text.split(maxsplit=2)
            if len(parts) >= 3:
                key, val = parts[1].lower(), parts[2]
                data[key] = val
                save_commands(data)
                await msg.reply(f"Command /{key} saved!")
            else:
                await msg.reply("Format salah. Gunakan /personal <command> <text>")

    @app.on_message(filters.command("unpersonal") & filters.private)
    async def delete_command(_, msg: Message):
        parts = msg.text.split()
        if len(parts) != 2:
            await msg.reply("Gunakan /unpersonal <command>")
            return
        key = parts[1].lower()
        data = load_commands()
        if key in data:
            del data[key]
            save_commands(data)
            await msg.reply(f"Command /{key} dihapus.")
        else:
            await msg.reply("Command tidak ditemukan.")
