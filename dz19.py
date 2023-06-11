import os
import logging
import random

from aiogram import Bot, Dispatcher, executor, types

from decouple import config

API_TOKEN = config('TELEGRAM_BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

problem1 = types.KeyboardButton('4 + 7 * 12')
problem2 = types.KeyboardButton('9 * 5')
problem3 = types.KeyboardButton('10 - 1 * 7')
problem4 = types.KeyboardButton('135 / 6')
problems = ['4 + 7 * 12', '9 * 5', '10 - 1 * 7', '135 / 6']
solution = 45

main_keyboard = types.ReplyKeyboardMarkup()
main_keyboard.add(problem1)
main_keyboard.add(problem2)
main_keyboard.add(problem3)
main_keyboard.add(problem4)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(solution, reply_markup=main_keyboard)
    @dp.message_handler()
    async def echo(message: types.Message):  
        if eval(message.text) == solution:
            await message.reply('correct!')
        else:
            await message.reply('incorrect!')

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Я бот для навчання Python")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    