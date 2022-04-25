from telethon import TelegramClient, events, sync
import trade
import tele
import time
import pyautogui
import psql

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

    try:
        if(len(var[0]) == 6 and (len(var[1]) == 3 or len(var[1]) == 4) and float(var[2]) and len(var[3]) == 2 and float(var[4]) and len(var[5]) == 2 and float(var[6]) and len(var[7]) == 2 and float(var[8]) and len(var[9]) == 2 and float(var[10])):
            order = trade.trade(var)
            if(order):
                psql.save_order(order, var)
                msg = "trade success"
        else:
            print("not buy signal")
            msg = "not buy signal "
    except Exception as err:

        print("not buy, err: ", err)
        msg = "not buy, err: " + err

    await client.send_file("Test", 'telegram.png')
    await client.send_file("Test", 'telegram2.png')
    await client.send_message("Test", var)
    await client.send_message("Test", msg)


client.start()
client.run_until_disconnected()
