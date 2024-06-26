from aiogram import Router
from .start import register_start_handler


def register_handlers(dp: Router):
    register_start_handler(dp)
