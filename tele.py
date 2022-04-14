from ctypes import resize
from turtle import heading, width
import pygetwindow
import pyautogui
from PIL import Image
import image


def screenshot():

    path = "/"

    titles = pygetwindow.getAllTitles()

    # x1,y1,width,height = pygetwindow.getWindowGeometry('Telegram')
    tt = pygetwindow.getWindowsWithTitle('Telegram')

    pyautogui.screenshot('telegram.png', region=(30, 309, 375, 160))
    pyautogui.screenshot('telegram2.png', region=(16, 460, 290, 120))

    img = Image.open('telegram.png')
   # print(img.height, " ", img.width)
    resized = img.resize((300, 120))
    resized.save('telegram.png')

    img = Image.open('telegram2.png')
  #  print(img.height, " ", img.width)
    resized = img.resize((750, 340))
    resized.save('telegram2.png')

    varray = []
    vsymbol = image.getIName('telegram.png').replace(
        " ", "").replace("/", "").replace("\n", "")

    varray.append(vsymbol)
    values = image.getIName('telegram2.png').split()

    varray.extend(values)

    print(varray)
    return varray


screenshot()
