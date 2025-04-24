from pyrogram import Client
from handlers import personal_command, call_command, unpersonal_command

app = Client("mybot", api_id=12345, api_hash="your_api_hash", bot_token="your_bot_token")

# Register all handlers
personal_command.add_handlers(app)
unpersonal_command.add_handlers(app)
call_command.add_handlers(app)

app.run()