from flask import Flask, request
from flask_cors import CORS, cross_origin
import trade
import tele
import time
import pyautogui
import psql
import dchat


app = Flask(__name__)
CORS(app)

# @app.route("/buy",methods= ["POST","GET"])
@app.route("/buy",methods= ["POST","GET"])
def buy():
    tel_event = request.json
    print("okey",tel_event['sl'])
    # msg = "null"
    # try:
    #     if(len(tel_event[0]) == 6 and (len(tel_event[1]) == 3 or len(tel_event[1]) == 4) and float(tel_event[2]) and len(tel_event[3]) == 2 and float(tel_event[4]) and len(tel_event[5]) == 2 and float(tel_event[6]) and len(tel_event[7]) == 2 and float(tel_event[8]) and len(tel_event[9]) == 2 and float(tel_event[10])):
    #         if tel_event[0] != "XAUUSD":
    #             tel_event[0] = tel_event[0] + '.tff'
    #         order = trade.trade(tel_event)
    #         msg = "order is null"
    #         if(order != None and order != 0):
    #             psql.save_order(order, tel_event)
    #             msg = "trade success"
    #     else:
    #         # print("okey not buy signal")
    #         msg = "not buy signal "
    # except Exception as err:

    #     # print("not buy, err: ", err)
    #     msg = "not buy, err: " + err
    return {"API":"Respoinse Positive"}


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5009)