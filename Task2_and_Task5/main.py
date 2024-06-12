import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from Task2_and_Task5.buttons import *
from text import *


TOKEN = "7351506393:AAH4UcHqZ-HVrc5ytxq8eCjkrDmf6p-V1VU"

dp = Dispatcher()


class Stepstate(StatesGroup):
    main = State()
    woman = State()
    start = State()
    man = State()
    duse = State()
    three = State()
    four = State()

@dp.message(CommandStart())
async def command_start_handler(message: Message,state:FSMContext) -> None:
    await state.set_state(Stepstate.main)
    cap = """
Assalomu alaykum ! 
Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib berad
    """
    await message.answer_photo(photo='https://telegra.ph/file/fe01b31e173a4eeff3282.png',caption=cap,reply_markup=await main_button())


@dp.message(Stepstate.main)
async def main_handler(msg : Message,state: FSMContext) -> None:
    if msg.text == admin_text:
        await msg.answer(f"{html.link(value= 'https://t.me/Absaitov_Dilshod',link='https://t.me/Absaitov_Dilshod')}",reply_markup=await main_button())
    elif msg.text == filial_text:
        await msg.answer_location(latitude=41.304476, longitude=69.253043,reply_markup=await main_button())

    elif msg.text == start_text:
        await state.set_state(Stepstate.start)
        await msg.answer("Quydagilardan birontasini tanlang 👇🏿",reply_markup=await start_button())



@dp.message(Stepstate.start)
async def start_handler(msg: Message,state: FSMContext) -> None:
    if msg.text == woman_text:
        await msg.answer("Vaqtim yetmadi bu qismini qilishga . Lekin originalida ham ishlamas ekan woman qismi")
    elif msg.text == man_text:
        await state.set_state(Stepstate.man)
        await msg.answer_photo(photo='https://telegra.ph/file/e4af69437d61cb5037730.png',caption='Quydagilarni birontasini tanlang 👇🏿',reply_markup=await woman_button())
    elif msg.text == back_text:
        await state.set_state(Stepstate.main)
        cap = """
Assalomu alaykum ! 
Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi
"""
        await msg.answer_photo(photo='https://telegra.ph/file/fe01b31e173a4eeff3282.png', caption=cap,
                                   reply_markup=await main_button())
        await state.set_state(Stepstate.main)


@dp.message(Stepstate.man)
async def man_handler(msg: Message,state : FSMContext) -> None:
    if msg.text == one_text:
        await state.set_state(Stepstate.duse)
        await msg.answer("Hafta kunlaridan birontasini tanlang",reply_markup=await week_button())

    elif msg.text == two_text:
        await state.set_state(Stepstate.duse)
        await msg.answer("Hafta kunlaridan birontasini tanlang", reply_markup=await week_button())
    elif msg.text == three_text:
        await state.set_state(Stepstate.three)
        await msg.answer("Hafta kunlaridan birontasini tanlang", reply_markup=await week_button())
    elif msg.text == four_text:
        await state.set_state(Stepstate.four)
        await msg.answer("Hafta kunlaridan birontasini tanlang", reply_markup=await week_button())
    elif msg.text == back_text:
        await state.set_state(Stepstate.start)
        await msg.answer_photo(photo='https://telegra.ph/file/33ef172b5f9ae1b08e160.png',
                               caption='Quydagilarni birontasini tanlang 👇🏿', reply_markup=await woman_button())


@dp.message(Stepstate.duse)
async def duse_handler(msg: Message,state: FSMContext) -> None:
    if msg.text == dush_text or msg.text == sesh_text:
        cap2 = """
4 x 10 tadan (ves ko'tara oladigan darajada bajariladi)
        """
        await msg.answer_photo(photo='https://telegra.ph/file/d6b50e46d389b48aa8a1c.png',caption=cap2)
        await msg.answer_photo(photo='https://telegra.ph/file/93f895626781b26312919.png',caption=cap2)
        await msg.answer_photo(photo='https://telegra.ph/file/0f45f19611107d0c97a17.png',caption=cap2)
        await msg.answer_photo(photo='https://telegra.ph/file/b49bb00622cb24b6e2fca.png',caption=cap2)
        await msg.answer_photo(photo='https://telegra.ph/file/fab1c7056e31d1469f23e.png',caption=cap2)
        await msg.answer_photo(photo='https://telegra.ph/file/1999901f3245a8a7860ac.png',caption=cap2)

    elif msg.text == chor_text or msg.text == pay_text:
        await msg.answer_photo(photo='https://telegra.ph/file/96bbd69c3b124300c38e6.png',caption="4 x 10 tadan (ves ko'tara oladigan darajada bajariladi)")
        await msg.answer_photo(photo='https://telegra.ph/file/9f5ea6924cebf9b691f73.png',caption="4 x 10 tadan (ves ko'tara oladigan darajada bajariladi)")
        await msg.answer_photo(photo='https://telegra.ph/file/a7f967697eb5ea927747e.png',caption="4 x 10 tadan (ves ko'tara oladigan darajada bajariladi)")
        await msg.answer_photo(photo='https://telegra.ph/file/4567f5e18024f783cdc69.png',caption="4 x 10 tadan (ves ko'tara oladigan darajada bajariladi)")
        await msg.answer_photo(photo='https://telegra.ph/file/bb985ccd19cd7c697adfe.png',caption="4 x 10 tadan (ves ko'tara oladigan darajada bajariladi)")
        await msg.answer_photo(photo='https://telegra.ph/file/56d1a6c0cbd813fd08620.png',caption="4 x 10 tadan (ves ko'tara oladigan darajada bajariladi)")

    elif msg.text == jum_text or shan_text:
        await msg.answer_photo(photo='https://telegra.ph/file/0c3d5965a8a98099ad976.png',caption="4 x 10 tadan (ves ko'tara oladigan darajada bajariladi)")
        await msg.answer_photo(photo='https://telegra.ph/file/1af2a38452fd0f21ee33c.png',caption="4 x 10 tadan (ves ko'tara oladigan darajada bajariladi)")
        await msg.answer_photo(photo='https://telegra.ph/file/a7f967697eb5ea927747e.png',
                               caption="4 x 10 tadan (ves ko'tara oladigan darajada bajariladi)")
        await msg.answer_photo(photo='https://telegra.ph/file/4567f5e18024f783cdc69.png',
                               caption="4 x 10 tadan (ves ko'tara oladigan darajada bajariladi)")
        await msg.answer_photo(photo='https://telegra.ph/file/bb985ccd19cd7c697adfe.png',
                               caption="4 x 10 tadan (ves ko'tara oladigan darajada bajariladi)")
        await msg.answer_photo(photo='https://telegra.ph/file/56d1a6c0cbd813fd08620.png',
                               caption="4 x 10 tadan (ves ko'tara oladigan darajada bajariladi)")
    elif msg.text == back_text:
        await state.set_state(Stepstate.man)
        await msg.answer_photo(photo='https://telegra.ph/file/e4af69437d61cb5037730.png',
                               caption='Quydagilarni birontasini tanlang 👇🏿', reply_markup=await woman_button())



@dp.message(Stepstate.three)
async def thre_handler(msg:Message,state:FSMContext)-> None:
    caption = """
5 x 15,18 tadan bajariladi (ves ko'tara oladigan darajada bajariladi)
    """
    if msg.text == dush_text or msg.text == sesh_text:
        await msg.answer_photo(photo='https://telegra.ph/file/d6b50e46d389b48aa8a1c.png', caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/93f895626781b26312919.png', caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/0f45f19611107d0c97a17.png', caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/b49bb00622cb24b6e2fca.png', caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/fab1c7056e31d1469f23e.png', caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/1999901f3245a8a7860ac.png', caption=caption)

    elif msg.text == chor_text or msg.text == pay_text:
        await msg.answer_photo(photo='https://telegra.ph/file/96bbd69c3b124300c38e6.png',caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/9f5ea6924cebf9b691f73.png',caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/a7f967697eb5ea927747e.png',caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/4567f5e18024f783cdc69.png',caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/bb985ccd19cd7c697adfe.png',caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/56d1a6c0cbd813fd08620.png',caption=caption)


    elif msg.text == jum_text or shan_text:
        await msg.answer_photo(photo='https://telegra.ph/file/0c3d5965a8a98099ad976.png',caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/1af2a38452fd0f21ee33c.png',caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/a7f967697eb5ea927747e.png',caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/4567f5e18024f783cdc69.png',caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/bb985ccd19cd7c697adfe.png',caption=caption)
        await msg.answer_photo(photo='https://telegra.ph/file/56d1a6c0cbd813fd08620.png',caption=caption)

    elif msg.text == back_text:
        await state.set_state(Stepstate.man)
        await msg.answer_photo(photo='https://telegra.ph/file/e4af69437d61cb5037730.png',
                               caption=caption, reply_markup=await woman_button())


@dp.message(Stepstate.four)
async def four_handler(msg:Message,state:FSMContext) -> None:
    caption1 = """
6 x 15,18 tadan bajariladi (ves ko'tara oladigan darajada bajariladi)
"""
    if msg.text == dush_text or msg.text == sesh_text:
        await msg.answer_photo(photo='https://telegra.ph/file/d6b50e46d389b48aa8a1c.png', caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/93f895626781b26312919.png', caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/0f45f19611107d0c97a17.png', caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/b49bb00622cb24b6e2fca.png', caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/fab1c7056e31d1469f23e.png', caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/1999901f3245a8a7860ac.png', caption=caption1)
    elif msg.text == chor_text or msg.text == pay_text:
        await msg.answer_photo(photo='https://telegra.ph/file/96bbd69c3b124300c38e6.png',caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/9f5ea6924cebf9b691f73.png',caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/a7f967697eb5ea927747e.png',caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/4567f5e18024f783cdc69.png',caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/bb985ccd19cd7c697adfe.png',caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/56d1a6c0cbd813fd08620.png',caption=caption1)


    elif msg.text == jum_text or shan_text:
        await msg.answer_photo(photo='https://telegra.ph/file/0c3d5965a8a98099ad976.png',caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/1af2a38452fd0f21ee33c.png',caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/a7f967697eb5ea927747e.png',caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/4567f5e18024f783cdc69.png',caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/bb985ccd19cd7c697adfe.png',caption=caption1)
        await msg.answer_photo(photo='https://telegra.ph/file/56d1a6c0cbd813fd08620.png',caption=caption1)

    elif msg.text == back_text:
        await state.set_state(Stepstate.man)
        await msg.answer_photo(photo='https://telegra.ph/file/e4af69437d61cb5037730.png',
                               caption=caption1, reply_markup=await woman_button())

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())