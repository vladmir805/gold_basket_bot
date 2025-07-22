from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛒 Привет! Я — GoldBasketBot. Готов к работе!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
