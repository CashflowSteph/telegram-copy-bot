from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

SOURCE_CHAT_ID = -1003390163313   # replace with your source ID
DEST_CHAT_ID = -1003840364408     # replace with your destination ID

async def copy_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == SOURCE_CHAT_ID:
        await context.bot.copy_message(
            chat_id=DEST_CHAT_ID,
            from_chat_id=SOURCE_CHAT_ID,
            message_id=update.message.message_id
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, copy_message))

app.run_polling()