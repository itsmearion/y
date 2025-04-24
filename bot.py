from pyrogram import Client
import config  # import dari config.py

from handlers import personal_command, call_command, unpersonal_command

app = Client(
    "mybot",
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token=config.bot_token
)

# Daftarkan semua handler
personal_command.add_handlers(app)
unpersonal_command.add_handlers(app)
call_command.add_handlers(app)

app.run()