import sys 
import trade

try:
    if sys.argv[3] == "goldinone":
        trade.goldbuyinone(sys.argv[1],int(sys.argv[2]))
        

except Exception as err:
    print("not buy, err: ", err)
    trade.goldbuy(sys.argv[1],int(sys.argv[2]))


    