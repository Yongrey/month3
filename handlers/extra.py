from aiogram import types, Dispatcher
from config import bot
from datetime import datetime, timedelta


async def ban_for_bad_words(message: types.Message):
    ban_words = ["damn", "fuck", "bitch"]
    for word in ban_words:
        if word in message.text.lower().replace(" ", ""):
            await  bot.ban_chat_member(message.chat.id, message.from_user.id, until_date=datetime.now() + timedelta(minutes=1))
            await bot.send_message(message.chat.id, f"Ban for the curse word, User:{message.from_user.full_name}")
            await bot.delete_message(message.chat.id, message.message_id)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(ban_for_bad_words)