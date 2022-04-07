api_id = 15397164
api_hash = '114a37cb56c089726d22431240b1080c'
from telethon.sync import TelegramClient, events

with TelegramClient('name',api_id, api_hash) as client:
    client.send_message('me','Hello myself!')
    print(client.download_profile_photo('me'))