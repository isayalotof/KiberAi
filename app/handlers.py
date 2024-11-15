from aiogram import F, Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, ContentType, FSInputFile, InputMediaPhoto
from aiogram.fsm.context import FSMContext
from app import keyboards as kb
from fsm.bot_fsm import ImgOrText
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        f'Рад тебя видеть {message.from_user.first_name.capitalize()}!\n'
        'Выбери режим для работы со мной',
        reply_markup=kb.main
    )
    await state.set_state(ImgOrText.neutral)

@router.message(F.text == 'Работа с текстом')
async def new_record(message: Message, state: FSMContext):
    await message.answer('Хорошо, давай начнем разговор!')
    await state.set_state(ImgOrText.text)


@router.message(F.text == 'Генерация изображений')
async def new_record(message: Message, state: FSMContext):
    await message.answer('Хорошо, что ты хочешь сгенерировать?')
    await state.set_state(ImgOrText.text)

