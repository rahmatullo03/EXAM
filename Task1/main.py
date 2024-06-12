
# Ozimni emailimni passwordini ololmadm
# shuning uchun sherigimni emailidan foydalandim


import asyncio
import logging
import sys

import smtplib, ssl
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

TOKEN = "6802211181:AAEct5JV8YedAOMDnSIzqTh4PDf8k-UnVTQ"




dp = Dispatcher()


class Stepstate(StatesGroup):
    email = State()

@dp.message(CommandStart())
async def command_start_handler(message: Message , state:FSMContext) -> None:
    await state.set_state(Stepstate.email)
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
    await message.answer("Email kiriting :")


@dp.message(Stepstate.email)
async def email_handler(msg : Message) -> None:
    port = 465
    smtp_server = "smtp.gmail.com"

    sender_email = "1999shohruhshahobiddinovich@gmail.com"
    receiver_email = f"{msg.text}"
    password = "xlugzkmfqmhlovkk"
    message = """ Python sila """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())