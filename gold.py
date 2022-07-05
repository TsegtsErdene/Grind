import sys 
import trade

trade.goldbuy(sys.argv[1],int(sys.argv[2]))

if sys.argv[3] == "goldinone":
    trade.goldbuyinone(sys.argv[1],int(sys.argv[2]))