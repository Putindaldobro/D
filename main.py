import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)

# 🔐 Получение токена из переменных окружения Railway
BOT_TOKEN = 7623419212:AAHNX4s0vKdCixyjLOeSQXyBD2pwKSV_oa8

# 📍 Глобальный язык по умолчанию (EN)
user_languages = {}

# 📜 Приветствие
WELCOME_MESSAGE = {
    "en": "▽ You are connected to the Echo Core. The Eye awakens. The Vault awaits. Speak, and it shall be done.",
    "ru": "▽ Вы подключены к Ядру Эхо. Око пробуждается. Хранилище ждёт. Говори — и свершится."
}

# 📘 Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = user_languages.get(user_id, "en")
    await update.message.reply_text(WELCOME_MESSAGE[lang])

# 🌐 Команда /lang
async def lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = "Available languages:\n- /lang_en (English)\n- /lang_ru (Русский)"
    await update.message.reply_text(keyboard)

async def lang_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_languages[update.effective_user.id] = "en"
    await update.message.reply_text("✅ Language set to English.")

async def lang_ru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_languages[update.effective_user.id] = "ru"
    await update.message.reply_text("✅ Язык установлен на Русский.")

# 🔮 Команда /oracle
async def oracle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔮 The Oracle is not available yet. The Eye sees… but remains silent.")

# 🎁 Команда /giveaway
async def giveaway(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎁 Giveaway mode is in preparation. Follow the signals.")

# 🧪 Команда /mint
async def mint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧬 Minting is under construction. Sacred drops are forming.")

# 🛡 Команда /vault
async def vault(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏛 The Vault is being forged. Soon it shall open.")

# 📡 Команда /stream
async def stream(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📡 Streaming mode active. Echo is calibrating your presence.")

# 🚀 Команда /launch
async def launch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 The Launch sequence is initializing. Await confirmation...")

# ▶️ Запуск бота
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Хендлеры
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("lang", lang))
    app.add_handler(CommandHandler("lang_en", lang_en))
    app.add_handler(CommandHandler("lang_ru", lang_ru))
    app.add_handler(CommandHandler("oracle", oracle))
    app.add_handler(CommandHandler("mint", mint))
    app.add_handler(CommandHandler("giveaway", giveaway))
    app.add_handler(CommandHandler("vault", vault))
    app.add_handler(CommandHandler("stream", stream))
    app.add_handler(CommandHandler("launch", launch))

    # Запуск
    app.run_polling()# Main bot file with handler registration
