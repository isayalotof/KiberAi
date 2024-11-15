from aiogram import Bot, Dispatcher
from config.cf import tg_token

bot = Bot(token=tg_token)
dp = Dispatcher()