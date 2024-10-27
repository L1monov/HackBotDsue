
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router, F

from settings import dict_faq

router_handlers = Router()

questions = list(dict_faq.keys())

@router_handlers.message(F.text.in_(questions))
async def set_mode_news(message: Message):
    """
    Настройка новостей
    :param message:
    :return:
    """
    text_msg = dict_faq[message.text]
    return await message.answer(text=text_msg)