from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message

from config_data.pass_gen import generate_password
from config_data.randon_choice import random_choice

router: Router = Router()


@router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(text=f'Привет {message.from_user.username},'
                              f' я магический шар, и я знаю ответ '
                              f'на любой твой вопрос')


@router.message(Text(endswith=['?'], ignore_case=False))
async def text_no_question(message: Message):
    await message.answer(text=random_choice())


@router.message(Command(commands=['password']))
async def send_command_password(message: Message):
    await message.answer(text='<b>Какой длинны пароль должен быть?</b>')


@router.message(lambda x: x.text.isdigit())
async def send_password(message: Message):
    await message.answer(text=generate_password(int(message.text)))
