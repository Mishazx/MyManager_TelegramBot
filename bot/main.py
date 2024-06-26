import asyncio
from aiogram import Bot, Dispatcher

from handlers import register_handlers
from session import bot


dp = Dispatcher()

register_handlers(dp)

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
