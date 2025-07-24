import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)

BOT_TOKEN = "7623419212:AAHNX4s0vKdCixyjLOeSQXyBD2pwKSV_oa8"
app = ApplicationBuilder().token(BOT_TOKEN).build()
