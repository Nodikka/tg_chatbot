import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from gpt_handler import handle_response



TOKEN = "BOT_TOKEN_HERE"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
  
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def message_handler(message: Message) -> None:
    try:
       message_type = message.chat.type
       text = (message.text).lower()
       user = message.from_user
       message_id = message.message_id
       response = ''

       print(f"User ({message.chat.id}) says: '{text}' in: '{message_type}'")
       response = handle_response(text, user, message_id)
       
       await message.answer(response)
    except AttributeError:
        print('')

async def main() -> None:
    
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())