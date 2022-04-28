from operator import mul
import pyautogui
import MetaTrader5 as mt
import trade
import psql
list = ['USDJPY', 'SELL', '128.05', 'TP', '127.85',
        'TP', '127.55', 'TP', '127.05', 'SL', '129.55']


psql.save_order(213122, list)


# try:
#     if(len(list[0]) == 6 and (len(list[1]) == 3 or len(list[1]) == 4) and float(list[2]) and len(list[3]) == 2 and float(list[4]) and len(list[5]) == 2 and float(list[6]) and len(list[7]) == 2 and float(list[8]) and len(list[9]) == 2 and float(list[10]) ):
#         order = trade.trade(list)


#     else:
#         print("false")
# except Exception as err:
#     print("not valid ",err)
