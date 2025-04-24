from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import personal, call_command

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

personal.add_handlers(app)
call_command.add_handlers(app)

app.run()