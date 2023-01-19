import json
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS, cross_origin
import MetaTrader5 as mt
import trade
import logging



log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


app = Flask(__name__)
CORS(app)

# @app.route("/buy",methods= ["POST","GET"])
# def sell():
#     tel_event = request.json
#     print(tel_event)
#     msg = "null"
#     try:
#         order = trade.trade(tel_event)
#         msg = "order is null"
#         # if(order != None and order != 0):
#         #     psql.save_order(order, tel_event)
#         #     msg = "trade success"
#     except Exception as err:

#         # print("not buy, err: ", err)
#         msg = "not buy, err: " + err
#     return {"API":"Respoinse Positive"}

@app.route("/buy",methods= ["POST","GET"])
def buy():
    tel_event = request.json
    # print(tel_event)
    msg = "null"
    try:
        order = trade.trade(tel_event)
        msg = "order is null"
        # if(order != None and order != 0):
        #     psql.save_order(order, tel_event)
        #     msg = "trade success"
        # print(order)
        return order
    except Exception as err:

        # print("not buy, err: ", err.message)
        return str(err) , 417
    
@app.route("/getPos",methods = ["POST","GET"])
def get_pos():
    data = {}
    jpos = []
    jord = []
    positions = mt.positions_get()
    orders = mt.orders_get()
    # print(orders)
    # print(positions)
    for pos in positions:
        jpos.append(pos._asdict())
    for order in orders:
        jord.append(order._asdict())
    data.update({"positions":jpos})
    data.update({"orders":jord})
    
    return jsonify(data)
if __name__ == '__main__':
    # app.run(host='0.0.0.0',port=5009, ssl_context=("cert.pem","key.pem") )
    app.run(host='0.0.0.0',port=5009 )