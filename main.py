import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = ApplicationBuilder().token(BOT_TOKEN).build()
