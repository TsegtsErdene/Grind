# import librariesyyyy
import MetaTrader5 as mt
import time
import sys
import psql
# connect Python to MetaTrader5
mt.initialize()


def trail_sl(pos):
    print(pos.type)
    
    item = psql.get(pos.ticket)
    if pos.type == 0:
        if(pos.price_current >= item[0][4]):
            print("buy")
    else:
        if(pos.price_current <= item[0][4] and pos.sl <= item[0][4]):
            print("true")
        print(pos)
        print(pos.price_current)
        print(item[0][4])

    # print(item)


if __name__ == '__main__':

    print('Starting Trailing Stoploss..')
    # strategy loop
    while True:
        positions = mt.positions_get()
        # check if position exists
        if positions:
            for pos in positions:
                trail_sl(pos)
            # wait 1 second
            # time.sleep(1)
        else:
            print('Position does not exist')
            sys.exit()
