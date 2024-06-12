from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from text import *


async def main_button():
    design = [
        [
            KeyboardButton(text=filial_text),
            KeyboardButton(text=start_text)
        ],
        [
            KeyboardButton(text=admin_text)
        ]
    ]
    rmk = ReplyKeyboardMarkup(keyboard=design,resize_keyboard=True)
    return rmk


async def start_button():
    design = [
        [
            KeyboardButton(text=woman_text),
            KeyboardButton(text=man_text)
        ],
        [
            KeyboardButton(text=back_text)
        ]
    ]
    rmk = ReplyKeyboardMarkup(keyboard=design,resize_keyboard=True)
    return rmk

async def woman_button():
    design = [
        [
            KeyboardButton(text=one_text),
            KeyboardButton(text=two_text)
        ],
        [
            KeyboardButton(text=three_text),
            KeyboardButton(text=four_text)
        ],
        [
            KeyboardButton(text=back_text)
        ]

    ]
    rmk = ReplyKeyboardMarkup(keyboard=design,resize_keyboard=True)
    return rmk

async def week_button():
    design = [
        [
            KeyboardButton(text=dush_text),
            KeyboardButton(text=sesh_text),
            KeyboardButton(text=chor_text),
        ],
        [
            KeyboardButton(text=pay_text),
            KeyboardButton(text=jum_text),
            KeyboardButton(text=shan_text),
        ],
        [
            KeyboardButton(text=back_text)
        ]

    ]
    rmk = ReplyKeyboardMarkup(keyboard=design,resize_keyboard=True)
    return rmk