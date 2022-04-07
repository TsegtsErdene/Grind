from ast import If
from turtle import position
import MetaTrader5 as mt
import pandas as pd
import plotly.express as px
from datetime import datetime
import constants

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


def calc_position_size(symbol, strategy):
    print("Calculating position size for: ", symbol)
    account = mt.account_info()
    balance = float(account.balance)
    print(balance)
    pip_value = constants.get_pip_value(symbol, strategy['account_currency'])
    print(pip_value)
    lot_size = (float(
        balance) * (float(strategy["risk"])/100)) / (pip_value * strategy["stopLoss"])
    lot_size = round(lot_size, 2)
    return lot_size


lot_size = calc_position_size('USDJPY', {
    "account_currency": "USD",
    "risk": 2,
    "stopLoss": 20})

print(lot_size)
