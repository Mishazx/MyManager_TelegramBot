import requests
from aiogram import Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import DOMAIN_SERVICE_URL
from utils.save_data_user import save_photo_user
from utils.request import RequestAPI


async def command_start_handler(message: Message) -> None:
    await save_photo_user(message)
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


async def link_account(message: Message):
    try:
        userid = message.from_user.id 

        # headers = {
        #     'Content-Type': 'application/json', 
        #     # 'Content-Type': 'application/json',  # Убедитесь, что заголовок Content-Type установлен
        #     'Authorization ': f'{API_SECRET_KEY}',  # Добавьте другие заголовки, если необходимо
        # }

        # response = requests.post(f"{DOMAIN_SERVICE_URL}/telegram/generate_link/", headers=headers, data={"userid": userid})
        url = "telegram/generate_link/"
        response = RequestAPI(url, method="POST", data={"userid": userid})
        # print()
        if response.status_code == 200:
            data = response.json()
            await message.reply(f"Please authenticate by following this link: {data['link']}")
            await message.reply(f"{data}")
        else:
            await message.reply(f"Failed to generate link. Please try again later. [{response.status_code}]")
    except Exception as e:
        await message.reply(f"Error: {e}")


def register_start_handler(router: Router):
    router.message.register(command_start_handler, CommandStart())
    router.message.register(link_account, Command(commands=["link"]))
    


