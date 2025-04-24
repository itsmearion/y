from pyrogram import Client, filters
import json
import os

API_ID = 24488567        # Ganti dengan API ID dari my.telegram.org
API_HASH = "51bb44c94b468bd8955f9e2916ed1402"  # Ganti dengan API Hash
BOT_TOKEN = "7674931376:AAHILgMWDqLsV-eKVJz4ARgETCIxC5B_Yi8"  # Ganti dengan token dari BotFather

app = Client("personal_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

DATA_FILE = "personal_data.json"
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        personal_data = json.load(f)
else:
    personal_data = {}

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(personal_data, f)

@app.on_message(filters.command("personal"))
async def personal_handler(client, message):
    try:
        _, keyword, *value = message.text.split()
        value = ' '.join(value)
        personal_data[keyword] = value
        save_data()
        await message.reply(f"Perintah /{keyword} disimpan!")
    except Exception:
        await message.reply("Format salah. Gunakan: /personal <keyword> <isi>")

@app.on_message(filters.command("unpersonal"))
async def unpersonal_handler(client, message):
    try:
        _, keyword = message.text.split()
        if keyword in personal_data:
            del personal_data[keyword]
            save_data()
            await message.reply(f"Perintah /{keyword} dihapus!")
        else:
            await message.reply("Keyword tidak ditemukan.")
    except Exception:
        await message.reply("Format salah. Gunakan: /unpersonal <keyword>")

@app.on_message(filters.command(""))
async def keyword_handler(client, message):
    keyword = message.command[0]
    if keyword in personal_data:
        await message.reply(personal_data[keyword])

app.run()