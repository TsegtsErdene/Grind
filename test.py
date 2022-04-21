import pyautogui

list = ["USDCAD", "BUY", "212.df", "23.34"]
try:
    if(len(list[0]) == 6 and float(list[3]) and (len(list[1]) == 3 or len(list[1]) == 4)):
        print("true")
        print(float(list[1]))
    else:
        print("false")
except:
    print("not valid")
