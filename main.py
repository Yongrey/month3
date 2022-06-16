from aiogram import types
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from handlers import client, callback_quiz, extra, admin, fsadmin_register
from config import bot, dp
from aiogram.utils import executor

client.register_handlers_client(dp)
admin.register_handler_admin(dp)
callback_quiz.register_handlers_callback_quiz(dp)
extra.register_handlers_extra(dp)
fsadmin_register.register_handler_registration(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
