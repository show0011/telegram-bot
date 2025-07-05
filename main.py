import asyncio
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = " 7785840491:AAFGIEgH1wXvyCpocWuPlEFDIcQ6ZqkYumQ" 

CHANNEL_USERNAME = "tajmines44"  # Номи канали Telegram (бе @)

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

user_state = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_state[chat_id] = {
        "luckyjet_index": 0,
        "mines_index": 0,
        "registered": False
    }

    text = (
        "1️⃣ Ба канал обуна шавед ✅\n"
        f"👉 https://t.me/{CHANNEL_USERNAME}\n\n"
        "2️⃣ Бо ин силка регистрация кунед 💸\n"
        "👉 https://1waabf.top/"
    )
    await update.message.reply_text(text)

async def check_subscription_and_registration(chat_id: int, context: ContextTypes.DEFAULT_TYPE):
    try:
        member = await context.bot.get_chat_member(f"@{CHANNEL_USERNAME}", chat_id)
        is_member = member.status in ["member", "administrator", "creator"]
    except:
        is_member = False

    # Барои мисол, ҳоло мо танҳо обуна шуданро санҷидем
    # Санҷиши регистрация аз лиҳози API ё базавӣ нест,
    # пас мо фикр мекунем, ки корбар онро анҷом додааст (шаҳсӣ мекунед).
    is_registered = True  # Барои мисол, бояд бо API ё база санҷид.

    return is_member and is_registered

async def luckyjet_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    state = user_state.get(chat_id)

    if not state:
        await update.message.reply_text("Лутфан /start-ро пахш кунед ва аввал обуна ва регистрацияро анҷом диҳед.")
        return

    allowed = await check_subscription_and_registration(chat_id, context)
    if not allowed:
        await update.message.reply_text("Лутфан аввал ба канал обуна шавед ва регистрацияро анҷом диҳед.")
        return

    index = state["luckyjet_index"]
    signal = signals_luckyjet[index]
    await update.message.reply_text(signal)

    state["luckyjet_index"] = (index + 1) % len(signals_luckyjet)

async def mines_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    state = user_state.get(chat_id)

    if not state:
        await update.message.reply_text("Лутфан /start-ро пахш кунед ва аввал обуна ва регистрацияро анҷом диҳед.")
        return

    allowed = await check_subscription_and_registration(chat_id, context)
    if not allowed:
        await update.message.reply_text("Лутфан аввал ба канал обуна шавед ва регистрацияро анҷом диҳед.")
        return

    index = state["mines_index"]
    signal = signals_mines[index]
    await update.message.reply_text(f"𝒎𝒊𝒏𝒆𝒔📍\n{signal}")

    state["mines_index"] = (index + 1) % len(signals_mines)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("luckyjet", luckyjet_signal))
    app.add_handler(CommandHandler("mines", mines_signal))

    app.run_polling()
