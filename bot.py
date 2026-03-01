from telegram.ext import ApplicationBuilder, MessageHandler, filters
import os

TOKEN = os.environ["BOT_TOKEN"]
SOURCE = int(os.environ["SOURCE"])
DEST = int(os.environ["DEST"])

app = ApplicationBuilder().token(TOKEN).build()

async def copy(update, context):
    if update.channel_post:
        await context.bot.copy_message(
            chat_id=DEST,
            from_chat_id=SOURCE,
            message_id=update.channel_post.message_id
        )

app.add_handler(MessageHandler(filters.ALL, copy))

app.run_polling()
