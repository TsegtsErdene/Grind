# import librariesyyyy
from email.policy import default
import MetaTrader5 as mt
import time
import sys
import psql
import dchat

# connect Python to MetaTrader5
mt.initialize()


def trail_sl(pos):

    item = psql.get(pos.ticket)

    if pos.type == 0:
        if(pos.price_current >= item[0][4] and round(pos.sl, 4) > item[0][3]):

            send_order(item[0][1], "tp1 reachaed", item[0][6], item[0][3])

    else:
        if(pos.price_current <= item[0][4] and round(pos.sl, 4) > item[0][3]):

            send_order(item[0][1], "tp1 reachaed", item[0][6], item[0][3])


def send_order(symbol, signal, tp, sl):

    msg = None
    request = {
        'action': mt.TRADE_ACTION_SLTP,
        'position': pos.ticket,
        'tp': float(tp),
        'sl': float(sl),

    }
    result = mt.order_send(request)

    match result.retcode:
        case 10009:
            msg = symbol + " " + signal
            print("send message success")

        case 10016:
            msg = symbol + " invalid stop"
            print("send invalid stop")
        case 10025:
            msg = symbol + " no change"
            print("send no change")
        case unknown_command:
            msg = symbol + " " + unknown_command
            print(unknown_command)

    dchat.send_discord(msg)


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
