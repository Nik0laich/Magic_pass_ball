from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

big_botton_1: InlineKeyboardButton = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='big_button_1_pressed'
)
big_botton_2: InlineKeyboardButton = InlineKeyboardButton(
    text='БОЛШАЯ КНОПКА 2',
    callback_data='big_button_2_pressed'
)

my_inline_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [big_botton_1], [big_botton_2]
    ]
)