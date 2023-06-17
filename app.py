from flask import Flask,request
from test1 import ทำคำสั่ง
from cryptotrade import checkAccount , openlong , openshort , closelong , closeshort
from Settrade import Set_spot_closelong , Set_spot_openlong
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! 123456</p>"

@app.route("/crypto",methods=["POST"])
def binance_trade_future():
    signal = json.loads(request.data)
    pair = signal["pair"] # BTCUSDT
    amount = signal["amount"] # 0.1
    action = signal["action"] # OPEN LONG , OPEN SHORT , TPSL LONG , TPSL SHORT
    
    partial_takeprofit = 100
    try:
        partial_takeprofit = int(signal["action"].split(" ")[-1]) 
    except:
        pass

    if action == "OPEN LONG":
        openlong(symbol=pair,amount=amount)
    
    elif action == "OPEN SHORT":
        openshort(symbol=pair,amount=amount)
        
    if "TPSL LONG" in action:
        closelong(symbol=pair,amount=float(amount)*partial_takeprofit/100)
    
    elif "TPSL SHORT" in action:
        closeshort(symbol=pair,amount=float(amount)*partial_takeprofit/100)

    return "200"

# @app.route("/settrade/future",methods=["POST"])
# @app.route("/forex/future",methods=["POST"])

@app.route("/settrade/spot",methods=["POST"])
def settrade_spot():
    signal = json.loads(request.data)
    pair = signal["pair"] # BTCUSDT
    amount = signal["amount"] # 0.1
    action = signal["action"] # OPEN LONG , OPEN SHORT , TPSL LONG , TPSL SHORT
    
    partial_takeprofit = 100
    try:
        partial_takeprofit = int(signal["action"].split(" ")[-1]) 
    except:
        pass
    
    if action == "OPEN LONG":
        Set_spot_openlong(symbol=pair,amount=amount)
    
    elif "CLOSE LONG" in action:
        Set_spot_closelong(symbol=pair,amount=amount)
    
    return "200"

@app.route("/check")
def checkuserBalance():
    return checkAccount()

# route forex
# route settrade

if __name__ == '__main__':
    app.run(debug=True)
    