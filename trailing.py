# import librariesyyyy
from email.policy import default
import MetaTrader5 as mt
import time
import sys
import psql
import dchat
import trade

# connect Python to MetaTrader5
mt.initialize()


def trail_sl(pos):
    item = psql.get(pos.ticket)

    if item:

        if pos.type == 0:  # BUY
            # tp 1 reached
            if(pos.price_current >= item[0][4] and round(pos.sl, 4) < item[0][3]):

                send_order(item[0][1
                                ], "tp1 reached", item[0][6], item[0][3], pos)

            # tp 2 reached
            elif(pos.price_current >= item[0][5] and round(pos.sl, 4) < item[0][4]):

                send_order(item[0][1], "tp2 reached", trade.pip_trail(
                    item[0][6], 40, 0), item[0][4], pos)

        else:  # Sell
            # tp 1 reached
            if(pos.price_current <= item[0][4] and round(pos.sl, 4) > item[0][3]):

                send_order(item[0][1], "tp1 reached", item[0][6], item[0][3], pos)

            # tp 2 reached
            elif(pos.price_current <= item[0][5] and round(pos.sl, 4) > item[0][4]):

                send_order(item[0][1], "tp2 reached", item[0][6], item[0][4], pos)


def send_order(tp, sl, ticket):

    msg = None
    request = {
        'action': mt.TRADE_ACTION_SLTP,
        'position': ticket,
        'tp': float(tp),
        'sl': float(sl),

    }
    result = mt.order_send(request)

    match result.retcode:
        case 10009:
            msg = ''
                       # print("send message success")

        case 10016:
            msg =  " invalid stop"
            # print("send invalid stop")
        case 10025:
            msg =  " no change"
            # print("send no change")
        case unknown_command:
            msg =  " " + unknown_command
            # print(unknown_command)

    dchat.send_discord(msg)

def trail_to_BE(pos):
    if pos.comment != '0' and pos.comment != '':
        if pos.type == 0: # BUY
            if float(pos.comment) <= pos.price_current:
                send_order(pos.tp,pos.price_open,pos.ticket)

        else: # SELL
            if float(pos.comment) >= pos.price_current:
                send_order(pos.tp,pos.price_open,pos.ticket)




if __name__ == '__main__':
    print('Starting Trailing Stoploss..')
    # strategy loop
    while True:
        positions = mt.positions_get()
        # check if position exists
        if positions:
            for pos in positions:
                trail_to_BE(pos)
            # wait 1 second
            time.sleep(1)
