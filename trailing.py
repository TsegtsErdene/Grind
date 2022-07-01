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

    item = psql.get_gold(pos.ticket)

    if pos.type == 0:  # BUY
        
        if(pos.price_current >= item[0][4] and round(pos.sl, 4) < item[0][3]):
            send_order("XAUUSD","tp1 reached",item[0][3],pos)
            psql.update_gold(pos.ticket,float(item[0][3]) + 1,float(item[0][4])+1)


    else:  # Sell
        # tp 1 reached
        if(pos.price_current <= item[0][4] and round(pos.sl, 4) > item[0][3]):
            #if(pos.price_current <= item[0][4] and round(pos.sl, 4) > item[0][3]):


            send_order("XAUUSD","tp1 reached",item[0][3],pos)
            psql.update_gold(pos.ticket,float(item[0][3]) - 1,float(item[0][4])-1)




def send_order(symbol, signal, sl, pos):

    msg = None
    request = {
        'action': mt.TRADE_ACTION_SLTP,
        'position': pos.ticket,
        'sl': float(sl)+0.2,

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
        cbuy = 0
        csell = 0
        # check if position exists
        if positions:
            for pos in positions:
                trail_sl(pos)

        #         if pos.type == 0:
        #             cbuy += 1
        #         elif pos.type == 1:
        #             csell += 1

        #     if cbuy == 0:
        #         trade.goldbuy('buy',1)
        #     elif csell == 0: 
        #         trade.goldbuy('sell',1)
        #         time.sleep(1)
        # else:
        #     trade.goldbuy('buy',1)
        #     trade.goldbuy('sell',1)
        # else:
        #     print('Position does not exist')
        #     sys.exit()
