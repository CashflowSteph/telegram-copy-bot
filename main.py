from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os, sys, socket


def singleton_lock(port=54321):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", port))
    except OSError:
        print("Another instance is already running. Exiting.")
        sys.exit(0)
    return s


lock_socket = singleton_lock()

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

SOURCE_CHAT_ID = int(os.getenv("SOURCE", "-1003390163313"))
DEST_CHAT_ID = int(os.getenv("DEST", "-1003840364408"))


async def copy_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    chat = update.effective_chat

    if not msg or not chat:
        return

    if chat.id != SOURCE_CHAT_ID:
        return

    await context.bot.copy_message(
        chat_id=DEST_CHAT_ID,
        from_chat_id=SOURCE_CHAT_ID,
        message_id=msg.message_id
    )


if __name__ == "__main__":
    print("Bot is starting...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, copy_message))
    app.run_polling(drop_pending_updates=True)
