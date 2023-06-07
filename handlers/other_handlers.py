from aiogram import Router
from aiogram.types import Message

router: Router = Router()


# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@router.message()
async def send_echo(message: Message):
    await message.answer(f'<b>Давай серьёзно...</b>\n\n'
                         f'Твоё сообщение\n '
                         f'<b>{message.text}</b> не похоже на вопрос\n'
                         f'поставь знак "?" в конце сообщения')
