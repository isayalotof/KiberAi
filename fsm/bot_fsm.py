from aiogram.fsm.state import StatesGroup, State

class ImgOrText(StatesGroup):
    unknown_user = State()
    neutral = State()
    img = State()
    text = State()
    bad_prompt = State()
    code_crash = State()
