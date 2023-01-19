from ast import If
from audioop import mul
from pickletools import markobject
from sre_constants import SUCCESS
from symtable import Symbol
from turtle import position
import MetaTrader5 as mt
import pandas as pd
import plotly.express as px
from datetime import datetime

mt.initialize()

#login = 1051435944
#password = "WLW2VB4M1R"
#server = "FTMO-Demo"

login = 1046294
password = "ldtkmDcxngHC50"
server = "TrueProprietaryFunds-Demo"

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
            # print('jpy')
            multiplier = 0.01
        else:
            multiplier = 0.0001
            # print('nrom')
        symbol_3 = "USD" + symbol_2

        try:
            varpip = price = mt.symbol_info_tick("USD" + symbol_2+".tff").ask
        except Exception:
            varpip = price
            # print('sorry')
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
    balance = float(10000)
    Value_per_pip = balance * 0.01 / stop_pip
    lot = (Value_per_pip * (100000 / varpip)) / 100000
    return round(lot, 2)


def tradebuy(symbol, type, stop_loss, take_profit, lotsize, orderT,pric,tp1):

    if orderT == False:
         #limit order
        if type == "BUY":
            type_trade = mt.ORDER_TYPE_BUY_LIMIT
        else:
            type_trade = mt.ORDER_TYPE_SELL_LIMIT

        request = {
            "action": mt.TRADE_ACTION_PENDING,
            "symbol": symbol,
            "volume": float(lotsize),
            "type": type_trade,
            "price": float(pric),
            "tp": float(take_profit),
            "sl": float(stop_loss),
            "deviation": 20,
            "comment":tp1,
            "magic": 234000,
        }
        
        order = mt.order_send(request)

        
    if orderT == True:
        #market buy
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
            "comment":tp1,
            "magic": 234000,
        }

        order = mt.order_send(request)

    # print(order)

    if order.retcode == 10015:
        raise Exception(order.comment)
    else:
        return order.comment


def trade(list):

    try:
        msg = []
        if(list['tp1'] != ''):
            order = tradebuy(list['symbol'], list['type'], list['sl'], list['tp1'], 0.3,list['order'],list['price'], list['tp1'])
            msg.append("TP1 " + order) 

        if(list['tp2'] != ''):
            order = tradebuy(list['symbol'], list['type'], list['sl'], list['tp2'], 0.2,list['order'],list['price'], list['tp1'])
            msg.append("TP2 " + order) 

        if(list['tp3'] != ''):
            order = tradebuy(list['symbol'], list['type'], list['sl'], list['tp3'], 0.1,list['order'],list['price'], list['tp1'])
            msg.append("TP3 " + order) 

        if not msg:
            raise Exception("TP алга бро")
        return msg

    except Exception as err:
        print("trade failed: ", err)
        raise err


def pip_trail(value, pip, type):
    if str(value).index('.') >= 2:  # JPY pair
        multiplier = 0.01
    else:
        multiplier = 0.01

    if(type == 0):
        value += pip * multiplier
    else:
        value -= pip * multiplier

    return value
