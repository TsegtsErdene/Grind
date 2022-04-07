from turtle import heading, width
import pygetwindow
import pyautogui
from PIL import Image
import image

path = "/"

titles = pygetwindow.getAllTitles()

# x1,y1,width,height = pygetwindow.getWindowGeometry('Telegram')
tt = pygetwindow.getWindowsWithTitle('Telegram')


pyautogui.screenshot('telegram.png',region=(30,277,379,100))
pyautogui.screenshot('telegram2.png',region=(15,410,200,130))

print(image.getIName('telegram.png'))
print(image.getIName('telegram2.png'))

# print(x1,y1,width,height)
