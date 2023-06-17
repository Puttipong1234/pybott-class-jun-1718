# signals = "OPENLONG BTCUSDT AT 25000"

# signals = signals.split("AT")

# print(signals) # ['OPENLONG', 'BTCUSDT', 'AT', '25000']

# action = signals[0]
# print(action)

# # Dictionary / Json ( javascript object notation )
# # key : value
# signals = { "a" : "ant" }
# print(signals["a"])

# signals = { "pair" : "BTCUSDT" , "amount" : 500 , "action" : "Open long"}
# pair = signals["pair"]
# amount = signals["amount"]
# action = signals["action"]

# print("ทำคำสั่งดังนี้")
# print("คู่เหรียญ : " + pair )
# print("ขนาดที่ซื้อ : " + str(amount) )
# print("เทรดฝั่ง : " + action )

# function
# x + y = 3
def ทำคำสั่ง(signals):
    pair = signals["pair"]
    amount = signals["amount"]
    action = signals["action"]

    print("ทำคำสั่งดังนี้")
    print("คู่เหรียญ : " + pair )
    print("ขนาดที่ซื้อ : " + str(amount) )
    print("เทรดฝั่ง : " + action )
    
    return 0

    
# data = { "pair" : "ETHUSDT" , "amount" : 200 , "action" : "Open long"}

# result = ทำคำสั่ง(signals=data)
# print(result)

# def ทำคำสั่ง(pair,amount,action):