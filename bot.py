from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Simpanan personal di memory
personal_data = {}

# Simpan keyword
async def personal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Gunakan format: /personal <keyword> <isi>")
        return

    keyword = context.args[0]
    value = ' '.join(context.args[1:])
    personal_data[keyword] = value
    await update.message.reply_text(f"Perintah /{keyword} disimpan!")

# Hapus keyword
async def unpersonal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Gunakan format: /unpersonal <keyword>")
        return

    keyword = context.args[0]
    if keyword in personal_data:
        del personal_data[keyword]
        await update.message.reply_text(f"Perintah /{keyword} dihapus!")
    else:
        await update.message.reply_text("Keyword tidak ditemukan.")

# Deteksi dan jalankan keyword
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lstrip('/')
    if text in personal_data:
        await update.message.reply_text(personal_data[text])

# Setup bot
async def main():
    app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

    app.add_handler(CommandHandler("personal", personal))
    app.add_handler(CommandHandler("unpersonal", unpersonal))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.COMMAND, handle_message))

    print("Bot berjalan...")
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())