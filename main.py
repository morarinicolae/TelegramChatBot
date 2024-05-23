import asyncio
from aiogram import Bot, Dispatcher, types

import os
from dotenv import load_dotenv

from loggin_config import get_logger

from app.handlers import router
from app.database.models import async_main


logger = get_logger(__name__)


async def main():
    load_dotenv(dotenv_path='.env')
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

    if not telegram_bot_token:
        raise ValueError("Nu s-a gasit Tokenul necesar")

    await async_main()
    bot = Bot(token=telegram_bot_token)
    logger.info("Botul sa initializat")
    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    logger.info("Botul a dat start!")
    await dispatcher.start_polling(bot)
    
    


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
