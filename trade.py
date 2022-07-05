from ast import If
from audioop import mul
from pickletools import markobject
from sre_constants import SUCCESS
from symtable import Symbol
from turtle import position
import MetaTrader5 as mt
import pandas as pd
import plotly.express as px
from psql import *
from datetime import datetime


mt.initialize()

# login = 1091062086 #main
# password = "FZRVX4CJZK"
# server = "FTMO-Server"

login = 1051200398 #alt
password = "9Y3SZBPAH9"
server = "FTMO-Demo"

mt.login(login, password, server)


def pip_value(symbol, type):
    symbol_1 = symbol[0:3]
    symbol_2 = symbol[3:6]

    if symbol_2 == "USD":
        return 10
    else:
        if type == "BUY" or type == "buy":
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
    balance = float(100000)
    Value_per_pip = balance * 0.05 / stop_pip
    lot = (Value_per_pip * (100000 / varpip)) / 100000
    return round(lot, 2)


def tradebuy(symbol, type, stop_loss, take_profit, lotsize):

    if type == "BUY" or type == "buy":
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

        order = tradebuy(list[0], list[1], list[10], list[8], lotSize)

        return order
    except Exception as err:
        print("trade failed: ", err)


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

def goldbuy(type,repeat = 1):

    if type == "BUY" or type == "buy":
        type_trade = mt.ORDER_TYPE_BUY
        price = mt.symbol_info_tick('XAUUSD').ask
        stoploss = price - 5
    else:
        type_trade = mt.ORDER_TYPE_SELL
        price = mt.symbol_info_tick('XAUUSD').bid
        stoploss = price + 5

    slpip = abs(DecToInt(stoploss) - DecToInt(price))

    lotSize = lot_value(slpip, pip_value('XAUUSD', type))

    request = {
        "action": mt.TRADE_ACTION_DEAL,
        "symbol": 'XAUUSD',
        "volume": float(lotSize),
        "type": type_trade,
        "price": price,
        "sl": float(stoploss),
        "deviation": 20,
        "magic": 234000,
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_IOC,
    }

    conn = None
    cur = None
    conn = pg.connect(host=host, dbname=db,user="postgres", password=123, port=5432)
    cur = conn.cursor()
    for i in range(int(repeat)):

        order = mt.order_send(request)

        if(order.order != None and order.order != 0):

            if type == "BUY" or type == "buy":

                stop = float(order.price) + 1

            else:
                stop = float(order.price) - 1
                
            save_gold(order.order, type_trade, order.price,stop ,conn,cur)

    cur.close()
    conn.close()

def goldbuyinone(type,repeat = 1):

    if type == "BUY" or type == "buy":
        type_trade = mt.ORDER_TYPE_BUY
        price = mt.symbol_info_tick('XAUUSD').ask
        stoploss = price - 5
    else:
        type_trade = mt.ORDER_TYPE_SELL
        price = mt.symbol_info_tick('XAUUSD').bid
        stoploss = price + 5

    slpip = abs(DecToInt(stoploss) - DecToInt(price))

    lotSize = lot_value(slpip, pip_value('XAUUSD', type)) * repeat

    request = {
        "action": mt.TRADE_ACTION_DEAL,
        "symbol": 'XAUUSD',
        "volume": float(lotSize),
        "type": type_trade,
        "price": price,
        "sl": float(stoploss),
        "deviation": 20,
        "magic": 234000,
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_IOC,
    }

    conn = None
    cur = None
    conn = pg.connect(host=host, dbname=db,user="postgres", password=123, port=5432)
    cur = conn.cursor()

    order = mt.order_send(request)

    if(order.order != None and order.order != 0):

        if type == "BUY" or type == "buy":

            stop = float(order.price) + 1

        else:
            stop = float(order.price) - 1
            
        save_gold(order.order, type_trade, order.price,stop ,conn,cur)

    cur.close()
    conn.close()

def close_position(position):

    tick = mt.symbol_info_tick(position.symbol)

    request = {
        "action": mt.TRADE_ACTION_DEAL,
        "position": position.ticket,
        "symbol": position.symbol,
        "volume": position.volume,
        "type": mt.ORDER_TYPE_BUY if position.type == 1 else mt.ORDER_TYPE_SELL,
        "price": tick.ask if position.type == 1 else tick.bid,
        "deviation": 20,
        "magic": 100,
        "comment": "thousand closed",
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_IOC,
    }

    order = mt.order_send(request)

    return order
