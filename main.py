from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Tu token del bot
BOT_TOKEN = "7107741381:AAHbcPjP6bnRBxhBcD5qE2H7d-KHDPvCwMg"

IMAGEN_URL = "https://cdn6.aptoide.com/imgs/8/8/8/88839b5183e85695750bae11545b870a_feature_graphic.png"

# Función de bienvenida con async y await correctamente usados
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎰 JUGAR", url="https://track.intrklnkmain.com/visit/?bta=37215&nci=5716")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    chat_id = update.effective_chat.id

    await context.bot.send_photo(chat_id=chat_id, photo=IMAGEN_URL)


    await update.message.reply_text(
        "🔥 <b>¡Bienvenido!🔥\n\n" \
        "1. ⬇️Registrate en el enlace de abajo⬇️\n" \
        "2. 💲Haz un deposito de la cantidad que desees💲\n" \
        "3. 🐥Busca <i>'chicken game'</i> en el buscador de la pagina🐥\n"
        "4. 💸¡Empieza a ganar dinero!</b>💸\n",parse_mode="HTML",
        reply_markup=reply_markup
    )

# Main del bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Bot corriendo... escribe /start en el chat con tu bot")
    app.run_polling()
