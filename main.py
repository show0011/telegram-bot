import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7785840491:AAFGIEgH1wXvyCpocWuPlEFDIcQ6ZqkYumQ"
CHANNEL_USERNAME = "tajmines44"

# Сигналҳои Lucky Jet
signals_luckyjet = [
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

# Сигналҳои MINES
signals_mines = [
    "кутиҳои 📍 6, 8,10,16 ⭐",
    "кутиҳои 📍 5,15,17,25 ⭐",
    "кутиҳои 📍 2,11,20,21 ⭐",
    "кутиҳои 📍 3,7,15,20 ⭐",
    "кутиҳои 📍 2,10,13,24 ⭐",
    "кутиҳои 📍 5,6,19,23 ⭐",
    "кутиҳои 📍 1,2,11,25 ⭐",
    "кутиҳои 📍 1,8,12,16 ⭐",
    "кутиҳои 📍 2,4,16,25 ⭐",
    "кутиҳои 📍 1,7,16,21 ⭐",
    "кутиҳои 📍 4,6,24,25 ⭐",
    "кутиҳои 📍 1,6,8,25 ⭐",
    "кутиҳои 📍 1,5,9,12 ⭐",
    "кутиҳои 📍 4,6,17,25 ⭐",
    "кутиҳои 📍 1,11,15,20 ⭐",
    "кутиҳои 📍 2,5,18,20 ⭐",
    "кутиҳои 📍 3,6,16,22 ⭐",
    "кутиҳои 📍 1,10,11,22 ⭐",
    "кутиҳои 📍 1,5,19,21 ⭐",
    "кутиҳои 📍 6,12,21,25 ⭐",
    "кутиҳои 📍 9,11,12,25 ⭐"
]

# Маълумоти корбарон
user_data = {}

# Санҷиши обуна
async def check_subscription(chat_id, bot):
    member = await bot.get_chat_member(f"@{CHANNEL_USERNAME}", chat_id)
    return member.status not in ["left", "kicked"]

# Амали старт
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_data[chat_id] = {"lj_idx": 0, "mine_idx": 0, "verified": False}

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("МАН ОБУНА ШУДАМ ✅", callback_data="verify")]
    ])
    await update.message.reply_text(
        f"1️⃣ Лутфан аввал ба канал обуна шавед: https://t.me/{CHANNEL_USERNAME}\n\n"
        "2️⃣ Пас аз обуна шудан, тугмаро пахш кунед.",
        reply_markup=keyboard
    )

# Амали тугмаҳо
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    await query.answer()

    # Агар тугмаи "МАН ОБУНА ШУДАМ ✅"
    if query.data == "verify":
        subscribed = await check_subscription(chat_id, context.bot)
        if not subscribed:
            await context.bot.send_message(chat_id, "❗ Шумо ҳоло ба канал обуна нашудаед: https://t.me/tajmines44")
            return

        user_data[chat_id]["verified"] = True
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("𝒍𝒖𝒄𝒌𝒚 𝒋𝒆𝒕📍", callback_data="luckyjet")],
            [InlineKeyboardButton("𝒎𝒊𝒏𝒆𝒔📍", callback_data="mines")]
        ])
        await context.bot.send_message(chat_id, "✅ Шумо муваффақона тасдиқ шудед! Тугмаҳоро зер кунед барои гирифтани сигнал:", reply_markup=keyboard)
        return

    if not user_data.get(chat_id, {}).get("verified"):
        await context.bot.send_message(chat_id, "❗ Лутфан аввал тугмаи 'МАН ОБУНА ШУДАМ ✅'-ро пахш кунед.")
        return

    if query.data == "luckyjet":
        idx = user_data[chat_id]["lj_idx"]
        await context.bot.send_message(chat_id, signals_luckyjet[idx])
        user_data[chat_id]["lj_idx"] = (idx + 1) % len(signals_luckyjet)
    elif query.data == "mines":
        idx = user_data[chat_id]["mine_idx"]
        await context.bot.send_message(chat_id, signals_mines[idx])
        user_data[chat_id]["mine_idx"] = (idx + 1) % len(signals_mines)

# Оғози бот
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()
