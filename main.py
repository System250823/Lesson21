import logging
from aiogram import Bot, Dispatcher, executor, types
from random import choice

API_TOKEN = '6152105477:AAGXcc_qWcv3CwpgO2AFQ0jI3CKkVQldORc'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привіт це перший бот на Python для телеграму!\n Зроблений HILLEL IT SCHOOL\n\n Напиши мені щось і я повторю твої слова!")
@dp.message_handler(commands=['help'])
async def send_rules(message: types.Message):
    await message.answer('Напиши мені будьке з цих питань:\nПривет\nКак дела?\nКакя погода за окном?\nКак тебя зовут?\nСколько тебе дней?\nКоторый час?')

answers = {
        'Привет' : 'Hello.txt',
        'Как дела?' : 'How are you.txt',
        'Какая погода за окном?' : 'Weather.txt', 
        'Как тебя зовут?' : 'Name.txt', 
        'Сколько тебе дней?' : 'How many days.txt',  
        'Который час?' : 'Time.txt',  
    }

@dp.message_handler()
async def get_random_response(message: types.Message):

    if message.text in answers:
        with open(f'Answers/{answers[message.text]}', 'r', encoding='utf-8') as file:
            some_answer = file.read().split('\n')
        await message.answer(choice(some_answer))
    else:
        await message.answer('Извините, я не могу ответить на этот вопрос в данный момент.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

