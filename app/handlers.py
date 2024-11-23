from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app import keyboards as kb
from fsm import bot_fsm as fsm
from app.bot import bot
from aiogram import types
from io import BytesIO
from app.getter import is_user

from tools.ai_requests.LLaMa_request import llama_req

from tools.ai_requests.Blackforest import get_photo

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    if is_user(message.from_user.id):
        ...
    else:
        # await message.answer(
        #     f'Рад тебя видеть {message.from_user.first_name.capitalize()}! 🤗\n'
        #     'Выбери режим для работы со мной👇',
        #     reply_markup=kb.main
        # )
        await message
    await state.set_state(fsm.ImgOrText.neutral)


@router.message(Command(commands=['Main_Menu']))

@router.message(F.text == 'Общение 💬')
async def new_record(message: Message, state: FSMContext):
    await message.answer('Хорошо, давай начнем разговор! 👋')
    await state.set_state(fsm.ImgOrText.text)


@router.message(F.text == 'Генерация изображений')
async def new_record(message: Message, state: FSMContext):
    await message.answer('Хорошо, что ты хочешь сгенерировать?')
    await state.set_state(fsm.ImgOrText.img)

@router.message(fsm.ImgOrText.text)
async def answer_for_user(message: Message):
    await message.answer('Думаю... 🤔')
    answer = llama_req(message.text)
    await message.answer(answer)


@router.message(fsm.ImgOrText.img)
async def generate_image(message: Message):
    await message.answer('Генерирую изображение... ⏳')
    photo = get_photo(message.text, str(message.from_user.id))
    await bot.send_photo(message.chat.id, photo=types.FSInputFile(photo))
