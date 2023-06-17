from flask import Flask,request
from test1 import ทำคำสั่ง
from cryptotrade import checkAccount , openlong , openshort , closelong , closeshort
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
    partial_takeprofit = int(signal["action"].split(" ")[-1]) 

    if action == "OPEN LONG":
        openlong(symbol=pair,amount=amount)
    
    elif action == "OPEN SHORT":
        openshort(symbol=pair,amount=amount)
        
    if "TPSL LONG" in action:
        closelong(symbol=pair,amount=float(amount)*partial_takeprofit/100)
    
    elif "TPSL SHORT" in action:
        closeshort(symbol=pair,amount=float(amount)*partial_takeprofit/100)

    return "200"

@app.route("/check")
def checkuserBalance():
    return checkAccount()

# route forex
# route settrade

if __name__ == '__main__':
    app.run(debug=True)
    