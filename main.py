import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main

import os
from dotenv import load_dotenv


async def main():
    await async_main()
    load_dotenv(dotenv_path='.env')
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not telegram_bot_token:
        raise ValueError("Nu s-a gasit Tokenul necesar") 
    bot = Bot(token=telegram_bot_token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
