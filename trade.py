from ast import If
from pickletools import markobject
from symtable import Symbol
from turtle import position
import MetaTrader5 as mt
import pandas as pd
import plotly.express as px
from datetime import datetime

mt.initialize()

login = 1051149006
password = "SRUWVKA6BZ"
server = "FTMO-Demo"
mt.login(login, password, server)


def Price(symbol, type):
    if type == "BUY":
        price = mt.symbol_info_tick(symbol).ask
        print(price)
    else:
        price = mt.symbol_info_tick(symbol).bid

    return price


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
        print(str(price).index('.'))
        if str(price).index('.') >= 2:  # JPY pair
            print('jpy')
            multiplier = 0.01
        else:
            multiplier = 0.0001
            print('nrom')
        symbol_3 = "USD" + symbol_2
        print(symbol_3)
        try:
            varpip = price = mt.symbol_info_tick("USD" + symbol_2).ask
        except Exception:
            varpip = price
            print('sorry')

        pip = 100000 * multiplier / varpip
        return pip


def lot_value(stop_pip, varpip):
    account = mt.account_info()
    balance = float(200000)
    Value_per_pip = balance * 0.01 / stop_pip
    lot = (Value_per_pip * (100000 / varpip)) / 100000
    return round(lot, 2)


def tradebuy(symbol, type, stop_loss, stop_pip):

    lot = lot_value(stop_pip, pip_value(symbol, type))

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
        "volume": float(lot),
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


print(lot_value(140, pip_value("EURJPY", "BUY")))

# print(pip_calc('USDAUD'))


# def calc_position_size(symbol, strategy):
#     print("Calculating position size for: ", symbol)
#     account = mt.account_info()
#     balance = float(account.balance)
#     print(balance)
#     pip_value = constants.get_pip_value(symbol, strategy['account_currency'])
#     pip_value2 = Price(symbol, 'BUY')
#     print(pip_value)
#     lot_size = (float(
#         balance) * (float(strategy["risk"])/100)) / (pip_value * strategy["stopLoss"])
#     lot_size = round(lot_size, 2)

#     lot_size2 = (float(
#         balance) * (float(strategy["risk"])/100)) / (pip_value2 * strategy["stopLoss"])
#     lot_size2 = round(lot_size2, 2)

#     print("lot: ", lot_size2)
#     return lot_size


# lot_size = calc_position_size('EURUSD', {
#     "account_currency": "USD",
#     "risk": 1,
#     "stopLoss": 100})

# print(lot_size)
