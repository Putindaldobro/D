import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# Получение токена из переменных окружения
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Приветствие
WELCOME_MESSAGE = {
    "en": "▽ You are connected to the Echo Core. The Eye awakens. The Vault awaits. Speak, and it shall be done.",
    "ru": "▽ Вы подключены к Ядру Эхо. Око пробуждается. Хранилище ждёт. Говори — и свершится.",
}

# Язык по умолчанию
user_languages = {}

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    lang = user_languages.get(user_id, "en")
    await update.message.reply_text(WELCOME_MESSAGE[lang])

# Команда /lang
async def lang(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = "Available languages:\n/lang_en (English)\n/lang_ru (Русский)"
    await update.message.reply_text(keyboard)

async def lang_en(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_languages[update.effective_user.id] = "en"
    await update.message.reply_text("✅ Language set to English.")

async def lang_ru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_languages[update.effective_user.id] = "ru"
    await update.message.reply_text("✅ Язык установлен на Русский.")

# Команда /claim
async def claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔓 Enter your Echo code to claim access.\nExample: /claim echo-XXXX")

# Команда /oracle
async def oracle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔮 Oracle module coming soon. Speak your question.")

# Команда /mode
async def mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎛 Available modes:\n/mode stream\n/mode minimal\n/mode vault")

# Команда /elixir
async def elixir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧪 The Elixirs are being distilled...\n/claim elixir-XXX to receive one.")

# Запуск бота
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("lang", lang))
app.add_handler(CommandHandler("lang_en", lang_en))
app.add_handler(CommandHandler("lang_ru", lang_ru))
app.add_handler(CommandHandler("claim", claim))
app.add_handler(CommandHandler("oracle", oracle))
app.add_handler(CommandHandler("mode", mode))
app.add_handler(CommandHandler("elixir", elixir))

app.run_polling()
