
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router, F
from aiogram.enums.parse_mode import ParseMode
from keyboards.keyboards import main_keyboard_conference_mode, keyboard_faq

from settings import *
main_commands_router = Router()

@main_commands_router.message(Command(commands=['start']))
async def set_mode_news(message: Message):
    """
    Настройка новостей
    :param message:
    :return:
    """
    keyboard = await main_keyboard_conference_mode()
    text_msg = "Привет. Я твой ассистент."
    return await message.answer(text=text_msg, reply_markup=keyboard)

@main_commands_router.message(F.text == 'Главное меню')
async def travel(message: Message):
    keyboard = await main_keyboard_conference_mode()
    text_msg = "Главное меню"
    return await message.answer(text=text_msg, reply_markup=keyboard)

@main_commands_router.message(F.text == '🚅Путешествие')
async def travel(message: Message):
    text_msg = traveling_text
    await message.answer(text=text_msg, parse_mode=ParseMode.MARKDOWN)

@main_commands_router.message(F.text == '💼Вакансии')
async def vacancies(message: Message):
    text_msg = vacancies_text
    await message.answer(text=text_msg, parse_mode=ParseMode.MARKDOWN)
@main_commands_router.message(F.text == '👨🏻‍💻Хакатоны')
async def hackathons(message: Message):
    text_msg = hackathons_text
    await message.answer(text=text_msg, parse_mode=ParseMode.MARKDOWN)

@main_commands_router.message(F.text == '📅Расписание')
async def schedule(message: Message):
    text_msg = schedule_text
    await message.answer(text=text_msg, parse_mode=ParseMode.MARKDOWN)

@main_commands_router.message(F.text == '🏠Жильё')
async def housing(message: Message):
    text_msg = housing_text
    await message.answer(text=text_msg, parse_mode=ParseMode.MARKDOWN)

@main_commands_router.message(F.text == '❓FAQ')
async def faq(message: Message):
    text = "Выбери вопрос"
    keyboard = await keyboard_faq()
    await message.answer(text=text, reply_markup=keyboard)


