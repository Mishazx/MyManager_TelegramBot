import logging
import asyncio
from aiogram import Dispatcher
from handlers import register_handlers
from session import bot


dp = Dispatcher()
register_handlers(dp)

async def on_startup(dp):
    logging.warning('Starting connection. ')

async def on_shutdown(dp):
    logging.warning('Shutting down..')
    logging.warning('Bye!')


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
