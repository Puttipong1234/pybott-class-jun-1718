import ccxt

# exchanges = ccxt.exchanges
# print(exchanges)

exchange = ccxt.binance({
    'apiKey':'0813c8e8f0ff67b903f4a6ee5bda3bf33ecf93324575aa59b154d049465dfcb0',
    'secret':'79cd1ee2e983d7b3ff99e968d3c08fbd55efe547ad00a33d694901929f4735e2',
    'options':{
        'defaultType':"future"
    }
})

exchange.set_sandbox_mode(True)


def checkAccount():
    account_data = exchange.fetch_balance()
    assets = account_data["info"]["assets"]

    text_display = ""
    
    for i in assets:
        text_display += i["asset"]
        text_display += i["walletBalance"]
        text_display += "\n"
    
    return text_display

def openlong(symbol,amount):
    param = {"positionSide":"LONG"}
    exchange.create_order(symbol=symbol,type="market",side="buy",amount=amount,params=param)

def closelong(symbol,amount):
    param = {"positionSide":"LONG"}
    exchange.create_order(symbol=symbol,type="market",side="sell",amount=amount,params=param)

def openshort(symbol,amount):
    param = {"positionSide":"SHORT"}
    exchange.create_order(symbol=symbol,type="market",side="sell",amount=amount,params=param)

def closeshort(symbol,amount):
    param = {"positionSide":"SHORT"}
    exchange.create_order(symbol=symbol,type="market",side="buy",amount=amount,params=param)

# perpetual future
# cross margin , hedge mode
# isolated margin , one way mode