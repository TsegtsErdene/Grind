import sys 
import trade

try:
    if sys.argv[3] == "goldinone":
        trade.goldbuyinone(sys.argv[1],int(sys.argv[2]))

except:
    trade.goldbuy(sys.argv[1],int(sys.argv[2]))


    