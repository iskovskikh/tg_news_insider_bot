from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section, as_key_value, HashTag
)

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Это новостной бот.\nДля просмотра списка команд введите /help')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        '/help - список команд'
    )

@router.message(Command("test1"))
async def cmd_test1(message: Message):
    await message.reply("Test 1")

@router.message(Command("test2"))
async def cmd_test2(message: Message):
    await message.reply("Test 2")


# https://mastergroosha.github.io/aiogram-3-guide/buttons/#inline-buttons