import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart

TOKEN = "8595486566:AAEyXAoB8xFV5SOXcdWZ_rqHUMHeGm-KkUs"

# Створення бота та диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Клавіатура
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привіт")],
        [KeyboardButton(text="Допомога")]
    ],
    resize_keyboard=True
)

# Обробник команди /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Привіт! Я бот на aiogram 🤖",
        reply_markup=keyboard
    )

# Обробник кнопки "Привіт"
@dp.message(F.text == "Привіт")
async def hello_handler(message: Message):
    await message.answer("І тобі привіт 👋")

# Обробник кнопки "Допомога"
@dp.message(F.text == "Допомога")
async def help_handler(message: Message):
    await message.answer("Я можу відповідати на повідомлення та кнопки.")

# Ехо-обробник (відповідає на будь-яке текстове повідомлення)
@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"Ти написав: {message.text}")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
