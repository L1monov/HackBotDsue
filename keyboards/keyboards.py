import asyncio

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.types import KeyboardButton

from settings import dict_faq

async def main_keyboard_conference_mode():
    builder = ReplyKeyboardBuilder()

    builder.add(KeyboardButton(text='🚅Путешествие'))
    builder.add(KeyboardButton(text='💼Вакансии'))
    builder.add(KeyboardButton(text='👨🏻‍💻Хакатоны'))
    builder.add(KeyboardButton(text="📅Расписание"))
    builder.add(KeyboardButton(text='🏠Жильё'))
    builder.add(KeyboardButton(text='❓FAQ'))

    builder.adjust(3)

    return builder.as_markup(resize_keyboard=True)

async def keyboard_faq():
    builder = ReplyKeyboardBuilder()

    for key, value in dict_faq.items():  # Используем .items() для доступа к ключам и значениям
        builder.add(KeyboardButton(text=key))

    builder.add(KeyboardButton(text="Главное меню"))
    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)


