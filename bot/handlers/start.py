import requests
from aiogram import Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import DOMAIN_SERVICE_URL
from utils.save_data_user import RequestCreateUser, save_photo_user
from utils.request import RequestAPI



async def command_start_handler(message: Message) -> None:
    await save_photo_user(message)
    data = await RequestCreateUser(message)
    await message.answer(f"Здравствуй, {html.bold(message.from_user.first_name)}! {data}")


async def link_account(message: Message):
    try:
        userid = message.from_user.id
        url = '/telegram/generate_link/'
        response = RequestAPI(url, method="POST", data={"userid": userid})
        if response.status_code == 200:
            data = response.json()
            await message.reply(f"Please authenticate by following this link: {data['link']}")
        else:
            raise Exception(f"Failed to generate link. Status code: {response.status_code}")
    except Exception as e:
        import traceback
        error_message = f"Error: {str(e).replace('<', '&lt;').replace('>', '&gt;')}"
        await message.reply(error_message)
        await message.reply(traceback.format_exc())


async def link_account(message: Message):
    try:
        userid = message.from_user.id 
        url = '/telegram/generate_link/'
        response = RequestAPI(url, method="POST", data={"userid": userid})
        if response.status_code == 200:
            data = response.json()
            await message.reply(f"Please authenticate by following [this link]({data['link']})", parse_mode='Markdown')
        else:
            await message.reply(f"Failed to generate link. Please try again later.")
    except Exception as e:
        await message.reply(f"Failed to generate link. Please try again later.")


async def unlink_account(message: Message):
    try:
        url = '/telegram/unlink/'
        data = f"{DOMAIN_SERVICE_URL}{url}"
        await message.reply(f"Unlinking your account... click to [this link]({data}) to unlink your account.")
    except Exception as e:
        await message.reply(f"Failed to unlink account. Please try again later.")



def register_start_handler(router: Router):
    router.message.register(command_start_handler, CommandStart())
    router.message.register(link_account, Command(commands=["link"]))
    router.message.register(unlink_account, Command(commands=["unlink"]))
    


