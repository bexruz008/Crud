from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards.default.menu import menu
from loader import dp


@dp.message_handler(Text(equals="Menu"))
async def get_menu(message:types.Message):
    await message.answer(text="Qaysi amalni tanlaysiz",
                         reply_markup=menu())






