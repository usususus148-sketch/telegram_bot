from telegram.ext import ApplicationBuilder, MessageHandler, filters

TOKEN = "8413647424:AAH0QQqzx8pf25NW_4zp4ZANZ3a5SR4GM60"

async def reply(update, context):
    await update.message.reply_text("البوت شغال يا معلم 🔥")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
app.run_polling()