from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from keyboards import admin_kb


class ShowsAdminStates(StatesGroup):
    photo = State()
    title = State()
    description = State()


async def is_admin_function(message: types.Message):
    global ADMIN_ID
    ADMIN_ID = 1150258083
    if message.from_user.id == ADMIN_ID:
        await bot.send_message(message.chat.id,
                               "Hello Admin, long time no see",
                               reply_markup=admin_kb.admin_markup)
    else:
        await bot.send_message(message.chat.id,
                               "Hello, u r not allowed to this function")
    await bot.delete_message(message.chat.id,
                             message.message_id)


async def cancel_command(message: types.Message,
                         state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.reply("State is None, Relax")
    await state.finish()
    await message.reply("Admin, relax, states cancelled successfully")


async def fsm_start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await ShowsAdminStates.photo.set()
        await message.reply("Admin, send me photo please")


async def load_photo(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await ShowsAdminStates.next()
    await message.reply("Admin, send me title of photo")


async def load_title(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    await ShowsAdminStates.next()
    await message.reply("Admin, send me description of photo, please")


async def load_description(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        await message.reply(str(data))


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(is_admin_function, commands=['admin'])
    dp.register_message_handler(cancel_command, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_command, Text(
        equals='cancel', ignore_case=False),
                                state='*')
    dp.register_message_handler(fsm_start,
                                commands=['upload'],
                                state=None)
    dp.register_message_handler(load_photo,
                                content_types=['photo'],
                                state=ShowsAdminStates.photo)
    dp.register_message_handler(load_title,
                                content_types=['text'],
                                state=ShowsAdminStates.title)
    dp.register_message_handler(load_description,
                                content_types=['text'],
                                state=ShowsAdminStates.description)