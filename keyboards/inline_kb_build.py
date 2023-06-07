from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

# from lexicon.lexicon import LEXICON


def create_inline_kb(width: int,
                     last_btn: str | None = None,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:

    kb_builber: InlineKeyboardBuilder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    kb_builber.row(*buttons, width=width)

    if last_btn:
        kb_builber.row(InlineKeyboardButton(
            text=last_btn,
            callback_data='last_btn'
        ))

    return kb_builber.as_markup()