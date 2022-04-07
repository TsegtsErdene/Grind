from ast import If
from turtle import position
import MetaTrader5 as mt
import pandas as pd
import plotly.express as px
from datetime import datetime

mt.initialize()

login = 61059970
password = "Empa2021*"
server = "Pepperstone-Demo"
mt.login(login, password, server)


def tradebuy(symbol, volume, type):

    if type == "BUY":
        type_trade = mt.ORDER_TYPE_BUY
        price = mt.symbol_info_tick(symbol).ask
        print(price)
    else:
        type_trade = mt.ORDER_TYPE_SELL
        price = mt.symbol_info_tick(symbol).bid
    request = {
        "action": mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": float(volume),
        "type": type_trade,
        "price": price,
        "tp": 46600.00,
        "deviation": 20,
        "magic": 234000,
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_IOC,
    }

    order = mt.order_send(request)
    print(order)


positions = mt.positions_get()
for pos in positions:
    print(pos.ticket)
# price = mt.symbol_info_tick("BTCUSD").ask
# print("asdsa", price)

# sltp_request = {
#     "action": mt.TRADE_ACTION_SLTP,
#     "symbol": symbol,
#     "volume": 0.03,
#     "type": mt.ORDER_TYPE_SELL,
#     "position": 36545450,
#     "sl": 20,
#     "price": mt.symbol_info_tick(symbol).ask,
#     "magic": 234000,
#     "comment": "Change stop loss",
#     "type_time": mt.ORDER_TIME_GTC,
#     "type_filling": mt.ORDER_FILLING_IOC,
# }
