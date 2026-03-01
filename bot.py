from telegram.ext import ApplicationBuilder, MessageHandler, filters
import os

app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

SOURCE = int(os.getenv("SOURCE"))
DEST = int(os.getenv("DEST"))

async def copy(update, context):
    if update.channel_post:
        await context.bot.copy_message(
            chat_id=DEST,
            from_chat_id=SOURCE,
            message_id=update.channel_post.message_id
        )

app.add_handler(MessageHandler(filters.ALL, copy))
app.run_polling()
