import MetaTrader5 as mt
import pandas as pd
import plotly.express as px
from datetime import datetime
import time

mt.initialize()

login = 21632227
password = 'Blackstar15'
server = 'Deriv-Demo'

mt.login(login, password, server)

account_info = mt.account_info()

num_symbols = mt.symbols_total()


def tradebuy(symbol, type, lotsize):

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
        "deviation": 20,
        "magic": 234000
    }

    order = mt.order_send(request)

    return order.order


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
    }

    order = mt.order_send(request)

    return order


def get_sym():
    symbols = mt.symbol_info("Crash 300 Index")
    now = symbols.ask

    return



