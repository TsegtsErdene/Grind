from ast import If
from pickletools import markobject
from sre_constants import SUCCESS
from symtable import Symbol
from turtle import position
import MetaTrader5 as mt
import pandas as pd
import plotly.express as px
from datetime import datetime

mt.initialize()

login = 1051158286
password = "LT5FCYR8BM"
server = "FTMO-Demo"
mt.login(login, password, server)


def pip_value(symbol, type):
    symbol_1 = symbol[0:3]
    symbol_2 = symbol[3:6]

    if symbol_2 == "USD":
        return 10
    else:
        if type == "BUY":
            price = mt.symbol_info_tick(symbol).ask
        else:
            price = mt.symbol_info_tick(symbol).bid

        if str(price).index('.') >= 2:  # JPY pair
            print('jpy')
            multiplier = 0.01
        else:
            multiplier = 0.0001
            print('nrom')
        symbol_3 = "USD" + symbol_2

        try:
            varpip = price = mt.symbol_info_tick("USD" + symbol_2).ask
        except Exception:
            varpip = price
            print('sorry')

        pip = 100000 * multiplier / varpip
        return pip


def DecToInt(var):
    if str(var).index('.') >= 2:  # JPY pair
        multiplier = 100
    else:
        multiplier = 10000
    var = float(var) * multiplier
    return int(var)


def lot_value(stop_pip, varpip):
    account = mt.account_info()
    balance = float(account.balance)
    Value_per_pip = balance * 0.01 / stop_pip
    lot = (Value_per_pip * (100000 / varpip)) / 100000
    return round(lot, 2)


def tradebuy(symbol, type, stop_loss, take_profit, lotsize):

    if type == "BUY":
        type_trade = mt.ORDER_TYPE_BUY
        price = mt.symbol_info_tick(symbol).ask
    else:
        type_trade = mt.ORDER_TYPE_SELL
        price = mt.symbol_info_tick(symbol).bid

    request = {
        "action": mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": float(lotsize),
        "type": type_trade,
        "price": price,
        "tp": float(take_profit),
        "sl": float(stop_loss),
        "deviation": 20,
        "magic": 234000,
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_IOC,
    }

    order = mt.order_send(request)

    return order.order


def trade(list):

    try:
        slpip = abs(DecToInt(list[2]) - DecToInt(list[10]))

        lotSize = lot_value(slpip, pip_value(list[0], list[1]))

        order = tradebuy(list[0], list[1], list[10], list[4], lotSize)

        return order
    except Exception as err:
        print("trade failed: ", err)
