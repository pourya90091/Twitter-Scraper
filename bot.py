import logging

from aiogram import Bot, Dispatcher, executor, types

from utils.utils import send_email
from utils.enigma.enigma_code_decode import code as encode, rotors_config as true_rotors_config
import settings
import os
import re
import json


tweets_dir = f'{settings.BASE_DIR}/core/tweets'

users = {}

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=settings.API_TOKEN)
disp = Dispatcher(bot)


@disp.message_handler(commands=['start', 'help', 'commands'])
async def start(message: types.Message):
    await message.answer('''    
    Commands:
    /config - Input : Three integer number (1 2 3).
    /email - Input : An authorized email address.
    /secret - Input : Password (helloworld).
    /twitter - Input : A Twitter account ID (1500tasvir).
    ''')


@disp.message_handler(commands=['email'])
async def email(message: types.Message):
    if re.search(r'^/email (.+)$', message.text):
        email = re.findall(r'^/email (.+)$', message.text)[0]
    else:
        return 1

    if email in settings.WHITELIST:
        send_email(settings.EMAIL, email, settings.PASSWORD, 'True Rotors Config', str(true_rotors_config))
        await message.answer('Email sent.')
    else:
        await message.answer('Access denied.')


@disp.message_handler(commands=['config'])
async def config(message: types.Message):
    user_id = str(message.from_id)

    if re.search(r'^/config (.+)$', message.text):
        config = re.findall(r'^/config (.+)$', message.text)[0]
    else:
        return 1

    config = config.split(' ')

    if len(config) != 3:
        await message.answer('Config include three integer number.')
        return 1

    rotors_config = []
    for num in config:
        try:
            rotors_config.append(int(num))
        except ValueError:
            await message.answer("Config's arguments must be integer number.")
            return 1

    users[user_id] = {
        'authorized': False,
        'rotors_config': tuple(rotors_config)
    }

    await message.answer(f'Your config are set ({", ".join(config)}).')


@disp.message_handler(commands=['secret'])
async def secret(message: types.Message):
    user_id = str(message.from_id)

    if user_id not in users.keys():
        return 1

    if users[user_id]['authorized']:
        await message.answer('You are already authorized.')
        return 0

    if re.search(r'^/secret (.+)$', message.text):
        secret = re.findall(r'^/secret (.+)$', message.text)[0]
    else:
        return 1

    code = encode(secret.lower(), users[user_id]['rotors_config'])
    true_code = encode(settings.SECRET, true_rotors_config)

    if code != true_code:
        await message.answer('Access denied.')
    else:
        users[user_id]['authorized'] = True
        await message.answer('You are authorized.')


@disp.message_handler(commands=['twitter'])
async def twitter(message: types.Message):
    user_id = str(message.from_id)

    if user_id not in users.keys():
        return 1

    if users[user_id]['authorized']:
        if re.search(r'^/twitter (.+)$', message.text):
            account = re.findall(r'^/twitter (.+)$', message.text)[0]
        else:
            return 1

        if f'{account}.json' in os.listdir(tweets_dir):
            with open(f'{tweets_dir}/{account}.json', 'r') as file:
                tweets = json.load(file)
        else:
            return 1

        for tweet in tweets:
            tweet_body = ''

            if tweet['event']:
                tweet_body += f'{tweet["event"]}\n'

            tweet_body += f'\n{tweet["owner"]} - {tweet["time"]}\n'
            tweet_body += f'\n{tweet["text"]}'

            await message.answer(tweet_body)
        else:
            return 1
    else:
        await message.answer('You are not authorized.')


if __name__ == '__main__':
    try:
        executor.start_polling(disp, skip_updates=True)
    except (Exception, KeyboardInterrupt) as err:
        if type(err) is KeyboardInterrupt:
            err = 'Interrupted'
        print('\nError:', err)
        exit()
