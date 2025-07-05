
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7785840491:AAFGIEgH1wXvyCpocWuPlEFDIcQ6ZqkYumQ"  

signals = [
    "𝐬𝐢𝐠𝐧𝐚𝐥.жди до х1.75",
    "𝐬𝐢𝐠𝐧𝐚𝐥.жди до х1.45",
    "𝐬𝐢𝐠𝐧𝐚𝐥.жди до х1.55",
    "𝐬𝐢𝐠𝐧𝐚𝐥.жди до х1.85",
    "𝐬𝐢𝐠𝐧𝐚𝐥.жди до х2.20",
    "𝐬𝐢𝐠𝐧𝐚𝐥.жди до х2.55",
    "𝐬𝐢𝐠𝐧𝐚𝐥.жди до х1.25",
    "𝐬𝐢𝐠𝐧𝐚𝐥.жди до х1.45",
    "𝐬𝐢𝐠𝐧𝐚𝐥.жди до х3.00",
    "𝐬𝐢𝐠𝐧𝐚𝐥.жди до х2.00",
    "𝐬𝐢𝐠𝐧𝐚𝐥.жди до х5.20",
    "𝐬𝐢𝐠𝐧𝐚𝐥.жди до х4.55",
    "𝐬𝐢𝐠𝐧𝐚𝐥.жди до х1.30"
]

user_signal_index = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_signal_index[chat_id] = 0

    text = (
        "1️⃣ Ба канал обуна шавед ✅\n👉 https://t.me/tajmines44\n\n"
        "2️⃣ Бо ин силка регистрация кунед 💸\n👉 https://1waabf.top/\n\n"
        "Пас тугмаи зерро барои тасдиқ ва гирифтани сигналҳо пахш кунед."
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Ман обуна шудам ва регистрация кардам", callback_data="confirmed")]
    ])

    await update.message.reply_text(text, reply_markup=keyboard)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    await query.answer()

    if query.data == "confirmed":
        user_signal_index[chat_id] = 0
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("𝒍𝒖𝒄𝒌𝒚 𝒋𝒆𝒕📍", callback_data="luckyjet")]
        ])
        await query.edit_message_text("Ҳоло метавонед сигналҳоро гиред:", reply_markup=keyboard)

    elif query.data == "luckyjet":
        index = user_signal_index.get(chat_id, 0)
        if index >= len(signals):
            index = 0
        signal = signals[index]
        user_signal_index[chat_id] = index + 1
        await context.bot.send_message(chat_id=chat_id, text=signal)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.run_polling()
