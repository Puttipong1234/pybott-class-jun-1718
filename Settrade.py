app_id = "podzKYoZPAcfv6Ov"
app_secret = "AMaNJsFXVIzH4rcfB/FidA7pE1MYW4h0PBSW2MN1Aavi"

from settrade_v2 import Investor

investor = Investor(
    app_id=app_id,
    app_secret=app_secret,
    broker_id="SANDBOX",
    app_code="SANDBOX"
)

account = investor.Equity(account_no="pyybott-E")
# print(account.get_account_info())

# market = investor.MarketData()
# ohlcv = market.get_candlestick(symbol="GULF",interval="15m",limit=100)
# print(ohlcv)

# talib

def Set_spot_openlong(symbol,amount):
    print("open long")
    place_order = account.place_order(
                        side= "Buy",
                        symbol= symbol,
                        trustee_id_type= "Local",
                        volume= amount,
                        qty_open= 0,
                        price= 0,
                        price_type= "MP-MKT",
                        validity_type= "Day",
                        bypass_warning= False,
                        pin= "000000"
                        )
    
def Set_spot_closelong(symbol,amount):
    print("open short")
    
# def openshort(symbol,amount):
#     print("close long")
    
# def closeshort(symbol,amount):
#     print("close short")