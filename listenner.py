from msilib.schema import EventMapping
from pyparsing import Or
from telethon import TelegramClient, events, sync
import image
import curdate
import trade
import pyzda
# Remember to use your own values from my.telegram.org!
api_id = 15397164
api_hash = '114a37cb56c089726d22431240b1080c'
client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage)
async def my_event_handler(event):
    pyzda.screenshot()
    # filename = "gege.jpg"
    # await event.download_media(filename)
    # print(curdate.ctime())
    # print("")
    # volume = 0.06

    # symbol = image.getIName(filename).replace(
    #     " ", "").replace("/", "").replace("\n", "")
    # tel_event = event.raw_text.split()

    # if (tel_event[0] == "BUY" or tel_event[0] == "SELL"):
    #     trade.tradebuy(symbol, volume, tel_event[0])

    # print(symbol)
    print(event.raw_text)
    print()


client.start()
client.run_until_disconnected()
