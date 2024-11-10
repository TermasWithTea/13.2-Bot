import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram import Router
import asyncio

logging.basicConfig(level=logging.INFO)

api = ''
bot = Bot(token = api)
storage = MemoryStorage()
dp = Dispatcher(storage=MemoryStorage())
router = Router()

@router.message(Command('start'))
async def start_massage(message: types.Message):
    await message.reply('Привет! Я бот помогающий твоему здоровью.')

@router.message()
async def all_massage(message:types.Message):
    await message.reply('Введите команду /start, чтобы начать общение.')

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


