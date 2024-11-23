from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Общение 💬'), KeyboardButton(text='Генерация изображений 🖼️')]
    ],
    resize_keyboard=True
)
