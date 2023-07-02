import os
import logging
import random
from random import randint

from aiogram import Bot, Dispatcher, executor, types

from decouple import config

from random import randint

API_TOKEN = config('TELEGRAM_BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
def make_equation(prblms):
    symbols = ['+', '-', '*', '/']
    problem =  f'{randint(50, 100)} {symbols[randint(0, 3)]} {randint (1,50)}'
    prblms.append(problem)
    return problem

problems = []
main_keyboard = types.ReplyKeyboardMarkup()
solution = ''
def update():
    problem1 = types.KeyboardButton(make_equation(problems))
    problem2 = types.KeyboardButton(make_equation(problems))
    problem3 = types.KeyboardButton(make_equation(problems))
    problem4 = types.KeyboardButton(make_equation(problems))

    main_keyboard.add(problem1)
    main_keyboard.add(problem2)
    main_keyboard.add(problem3)
    main_keyboard.add(problem4)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    update()
    global solution
    solution = eval(random.choice(problems))
    await message.answer(solution, reply_markup=main_keyboard)

@dp.message_handler()  
async def isCorrect(message: types.Message):
    global solution
    if "*" in message.text or "+" in message.text or "-" in message.text or "/" in message.text:
        if eval(message.text) == solution:
            await message.reply('correct! /start for the next problem')
            solution = ''
            global problems
            problems = []
            main_keyboard.keyboard=[]
        else:
            await message.reply('incorrect!')
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)