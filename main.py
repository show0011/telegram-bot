import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7785840491:AAFGIEgH1wXvyCpocWuPlEFDIcQ6ZqkYumQ"  # Токени боти худро инҷо гузоред

CHANNEL_USERNAME = "tajmines44"  # Номи канали шумо бе @

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

signals_mines = [
    "кутихои 📍 6, 8,10,16  ⭐",
    "кутихои 📍 5,15,17,25 ⭐",
    "кутихои 📍 2,11,20,21 ⭐",
    "кутихои 📍 3,7,15,20  ⭐",
    "кутихои 📍 2,10,13,24 ⭐",
    "кутихои 📍 5,6,19,23 ⭐",
    "кутихои 📍  1,2,11,25 ⭐",
    "кутихои 📍 1,8,12,16 ⭐",
    "кутихои 📍 2,4,16,25 ⭐",
    "кутихои 📍 1,7,16,21 ⭐",
    "кутихои 📍 4,6,24,25 ⭐",
    "кутихои 📍 1,6,8,25 ⭐",
    "кутихои 📍  1,5,9,12 ⭐",
    "кутихои 📍  4,6,17,25 ⭐",
    "кутихои 📍  1,11,15,20 ⭐",
    "кутихои 📍  2,5,18,20 ⭐",
    "кутихои 📍  3,6,16,22  ⭐",
    "кутихои 📍  1,10,11,22 ⭐",
    "кутихои 📍  1,5,19,21 ⭐",
    "кутихои 📍  6,12,21,25⭐",
    "кутихои 📍  9,11,12,25 ⭐"
]

user_data = {}

async def check_subscription(chat_id, bot):
    member = await bot.get_chat_member(f"@{CHANNEL_USERNAME}", chat_id)
    return member.status != "left"  # Агар корбар обуна бошад, статусаш left нест

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_data[chat_id] = {"luckyjet_index": 0, "mines_index": 0, "registered": False}

    msg = (
        f"1️⃣ Ба канал обуна шавед ✅\n👉 https://t.me/{CHANNEL_USERNAME}\n\n"
        "2️⃣ Бо ин силка регистрация кунед 💸\n👉 https://1waabf.top/"
    )
    await update.message.reply_text(msg)

async def check_registration(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_data.setdefault(chat_id, {"luckyjet_index": 0, "mines_index": 0, "registered": False})
    user_data[chat_id]["registered"] = True
    await update.message.reply_text("Регистрацияи шумо сабт шуд! Акнун шумо сигналҳоро мегиред.")

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("𝒍𝒖𝒄𝒌𝒚 𝒋𝒆𝒕📍", callback_data="luckyjet")],
        [InlineKeyboardButton("𝒎𝒊𝒏𝒆𝒔📍", callback_data="mines")]
    ])
    await update.message.reply_text("Тугмаро пахш кунед барои гирифтани сигнал:", reply_markup=keyboard)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    chat_id = query.message.chat_id
    await query.answer()

    subscribed = await check_subscription(chat_id, context.bot)
    registered = user_data.get(chat_id, {}).get("registered", False)

    if not subscribed:
        await context.bot.send_message(chat_id, f"Лутфан аввал ба канал обуна шавед: https://t.me/{CHANNEL_USERNAME}")
        return
    if not registered:
        await context.bot.send_message(chat_id, "Лутфан аввал ба силкаи регистрация муроҷиат кунед: https://1waabf.top/")
        return

    if query.data == "luckyjet":
        idx = user_data[chat_id]["luckyjet_index"]
        await context.bot.send_message(chat_id, signals_luckyjet[idx])
        user_data[chat_id]["luckyjet_index"] = (idx + 1) % len(signals_luckyjet)

    elif query.data == "mines":
        idx = user_data[chat_id]["mines_index"]
        await context.bot.send_message(chat_id, signals_mines[idx])
        user_data[chat_id]["mines_index"] = (idx + 1) % len(signals_mines)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("register", check_registration))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot started...")
    app.run_polling()
