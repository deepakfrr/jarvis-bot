import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_USERNAME = os.getenv("OWNER_USERNAME")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton("📩 Contact Owner", url=f"https://t.me/{OWNER_USERNAME}")
    ]]
    await update.message.reply_text(
        "👋 Hello Sir.\n"
        "🧠 JΛЯVIS :: SYSTEM online\n"
        "⚙️ Awaiting your command.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"👤 System Admin: @{OWNER_USERNAME}"
    )

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Processing...\n"
        "AI module will be enabled soon."
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("owner", owner))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

print("JΛЯVIS :: SYSTEM running...")
app.run_polling()
