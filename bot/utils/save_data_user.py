import os
from aiogram.types import Message, UserProfilePhotos
from utils.request import RequestAPI
from session import bot

async def RequestCreateUser(message: Message):
    user_data = {
        "user": None, 
        "userid": message.from_user.id,
        "username": message.from_user.username,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "image_data": None
    }
    url = '/telegram/create_user/'
    response = RequestAPI(url, method="POST", data=user_data)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response)
        return response.status_code

async def save_photo_user(message: Message):
    userid = message.from_user.id
    user_profile_photo: UserProfilePhotos = await bot.get_user_profile_photos(userid)
    
    if len(user_profile_photo.photos) > 0 and len(user_profile_photo.photos[0]) > 0:
        file = await bot.get_file(user_profile_photo.photos[0][0].file_id)
        
        target_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'media'))
        os.makedirs(target_directory, exist_ok=True)
        
        target_path = os.path.join(target_directory, f'{userid}.png')
        
        await bot.download_file(file.file_path, target_path)
    else:
        print('У пользователя нет фото в профиле.')
