from pyrogram import Client
import config  # import dari config.py

from handlers import personal_command, call_command, unpersonal_command

app = Client(
    "mybot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# Daftarkan semua handler
personal_command.add_handlers(app)
unpersonal_command.add_handlers(app)
call_command.add_handlers(app)

app.run()