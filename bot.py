from pyrogram import Client, filters
from pyrogram.types import Message
import config

TEMPLATE = (
    "Salutations I'm @username, I’d like to place an order for catalog "
    "[t.me/catal] listed at Blakeshley, Using payment method "
    "[dana, gopay, qriss, spay, ovo, bank.] The total comes to IDR 00.000 "
    "Inrush add 5k [yay/nay]. Kindly process this, Thanks a bunch."
)

app = Client(
    "format_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

@app.on_message(filters.command("format", prefixes="/"))
async def format_cmd(_, msg: Message):
    if msg.edit_date:
        return
    await msg.reply(TEMPLATE, quote=True)  # autocopy via reply

if __name__ == "__main__":
    print(">> FormatBot running – press Ctrl‑C to stop.")
    app.run()