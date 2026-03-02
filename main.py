import os
from telegram.ext import ApplicationBuilder

TOKEN = os.environ.get("BOT_TOKEN")

print("TOKEN LENGTH:", len(TOKEN) if TOKEN else "NONE")
print("TOKEN RAW:", repr(TOKEN))

app = ApplicationBuilder().token(TOKEN).build()

print("Bot started successfully")
app.run_polling()
