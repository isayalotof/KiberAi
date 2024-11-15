from aiogram.fsm.state import StatesGroup, State

class ImgOrText(StatesGroup):
    img = State()
    text = State()
    neutral = State()