import MetaTrader5 as mt
import time
import sys
import psql
# connect Python to MetaTrader5
mt.initialize()


def trail_sl(pos):
    # print(pos.ticket)

    item = psql.get(pos.ticket)
    print(pos)
    # if pos.type == 0:
    #     if(pos.price_current >= item[0][4] and round(pos.sl, 4) > item[0][3]):
    #         request = {
    #             'action': mt.TRADE_ACTION_SLTP,
    #             'position': pos.ticket,
    #             'tp': float(item[0][6]),
    #             'sl': float(item[0][3]),

    #         }
    #         result = mt.order_send(request)

    #         match result.retcode:
    #             case 10009:
    #                 print("send message success")
    #             case 10016:
    #                 print("send invalid stop")
    #             case 10025:
    #                 print("send no change")
    #             case unknown_command:
    #                 print(unknown_command)
    # else:
    #     if(pos.price_current <= item[0][4] and round(pos.sl, 4) > item[0][3]):

    #         request = {
    #             'action': mt.TRADE_ACTION_SLTP,
    #             'position': pos.ticket,
    #             'tp': float(item[0][6]),
    #             'sl': float(item[0][3]),

    #         }
    #         result = mt.order_send(request)

    #         match result.retcode:
    #             case 10009:
    #                 print("send message success")
    #             case 10016:
    #                 print("send invalid stop")
    #             case 10025:
    #                 print("send no change")
    #             case unknown_command:
    #                 print(unknown_command)
        # print(item)
        # print(pos.price_current)
        # print(item[0][4])
        # print(" \space")

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
            time.sleep(1)
        else:
            print('Position does not exist')
            sys.exit()
