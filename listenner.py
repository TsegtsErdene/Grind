from msilib.schema import EventMapping
from turtle import circle
from pyparsing import Or
from telethon import TelegramClient, events, sync
import image
import trade
import tele
import time
import pyautogui
# Remember to use your own values from my.telegram.org!
api_id = 15397164
api_hash = '114a37cb56c089726d22431240b1080c'
client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage)
async def my_event_handler(event):

    pyautogui.click(483, 556)
    pyautogui.press('enter')
    time.sleep(2)
    tel_event = tele.screenshot()
    str1 = " "
    var = str1.join(tel_event)

    # volume = 0.06

    # symbol = image.getIName(filename).replace(
    #     " ", "").replace("/", "").replace("\n", "")
    # tel_event = event.raw_text.split()

    # if (tel_event[1] == "BUY" or tel_event[1] == "SELL"):
    #trade.tradebuy(symbol, volume, tel_event[0])
    await client.send_file("Test", 'telegram.png')
    await client.send_file("Test", 'telegram2.png')
    await client.send_message("Test", var)
    # print(symbol)


client.start()
client.run_until_disconnected()
