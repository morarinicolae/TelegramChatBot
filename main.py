import asyncio
from aiogram import Bot, Dispatcher, types

import os
from dotenv import load_dotenv

from app.handlers import router
from app.database.models import async_main


async def main():
    load_dotenv(dotenv_path='.env')
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

    if not telegram_bot_token:
        raise ValueError("Nu s-a gasit Tokenul necesar")

    await async_main()
    bot = Bot(token=telegram_bot_token)
    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    await dispatcher.start_polling(bot)
    
    


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
