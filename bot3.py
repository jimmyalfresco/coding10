from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

key_token = "6330501406:AAHayU2GWvtOiTAX6q_G34auaesfiYzrxp4"
user_bot = "immy_ay_bot"

async def start_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Selamat datang!")

async def help_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pilih (gunting / batu / kertas)")

async def text_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    text_diterima : str = update.message.text

    print(f"Pesan diterima : {text_diterima}")

    text_lwr_diterima = text_diterima.lower()

    if 'gunting' in text_lwr_diterima:
        await update.message.reply_text("batu")
    elif 'batu' in text_lwr_diterima:
        await update.message.reply_text("kertas")
    elif 'kertas' in text_lwr_diterima:
        await update.message.reply_text("gunting")
    elif 'kalah terus' in text_lwr_diterima:
        await update.message.reply_text("Saya pasti menang")
    else:
        await update.message.reply_text("hehe..")

async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")

if __name__ == '__main__':
    print("Mulai")

    app = Application.builder().token(key_token).build()
    #COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    #MESSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_message))
    #error :
    app.add_error_handler(error)
    #polling :
    app.run_polling(poll_interval=1)
