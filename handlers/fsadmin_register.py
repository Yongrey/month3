from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from keyboards import admin_kb


class ShowsUserStates(StatesGroup):
    username = State()
    User_first_name = State()
    User_last_name = State()








async def fsm_start(message: types.Message):
        await ShowsUserStates.username.set()
        await message.reply("Send me your username, please")





async def load_username(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:

        data['username'] = message.text
    if message.from_user.username == data:
        await ShowsUserStates.next()
        await message.reply("send me your first name")
    else:
        await message.reply("you sent not your username, please try again")



async def load_fname(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
        if message.from_user.first_name == data:
            await ShowsUserStates.next()
            await message.reply("send me your last name")
        else:
            await message.reply("you sent not your first name, please try again")


async def load_lastname(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
        if message.from_user.last_name_name == data:
            await message.reply(str(data))
        else:
            message.reply("you sent not your last name, please try again")


def register_handler_registration(dp: Dispatcher):

    dp.register_message_handler(fsm_start,
                                commands=['username'],
                                state=None)
    dp.register_message_handler(load_username,
                                state=ShowsUserStates.username)
    dp.register_message_handler(load_fname,
                                content_types=['text'],
                                state=ShowsUserStates.User_first_name)
    dp.register_message_handler(load_lastname,
                                content_types=['text'],
                                state=ShowsUserStates.User_last_name)