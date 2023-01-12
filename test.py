from operator import mul
import pyautogui
import MetaTrader5 as mt
# import pandas as pd
# import plotly.express as px
import trade
import psql
import json

list = ['CHFJPY', 'SELL', '136.35', 'TP', '136.15',
        'TP', '135.85', 'TP', '135.35', 'SL', '137.85']

# psql.save_order(41201381, list)


data = mt.symbol_info("XAUUSD")._asdict()
poss = mt.positions_get()
# print(data)

for pos in poss:

        print(pos._asdict(),"\n")


# request = {
#     'action': mt.TRADE_ACTION_SLTP,
#     'position': 9451540,
#     'tp': float(0.834),
# }

# result = mt.order_send(request)
# print(result)

# try:
#     if(len(list[0]) == 6 and (len(list[1]) == 3 or len(list[1]) == 4) and float(list[2]) and len(list[3]) == 2 and float(list[4]) and len(list[5]) == 2 and float(list[6]) and len(list[7]) == 2 and float(list[8]) and len(list[9]) == 2 and float(list[10]) ):
#         order = trade.trade(list)


#     else:
#         print("false")
# except Exception as err:
#     print("not valid ",err)
