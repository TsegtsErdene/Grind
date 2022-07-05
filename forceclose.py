import MetaTrader5 as mt
import time
import sys
import psql
# connect Python to MetaTrader5
mt.initialize()


def trail_sl(pos):

    if(pos.profit >= 500):
        close_position(pos)


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


if __name__ == '__main__':

    print('Close when thousand starting...')
    # strategy loop
    acc = mt.account_info()
    positions = mt.positions_get()
    try:
        if sys.argv[1] != None:
            for i in range(int(sys.argv[1])):
                if positions[i].symbol == "XAUUSD":
                    close_position(positions[i])
            sys.exit()
    except:
        while True:
         
            if positions:
                for pos in positions:
                    if pos.symbol == "XAUUSD":
                        close_position(pos)
            else:
                print('Position does not exist')
                sys.exit()

            time.sleep(1)
        
