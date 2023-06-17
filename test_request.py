#จำลองสัญญาณ
import requests

url = 'http://127.0.0.1:5000/crypto'
data = {'action': 'TPSL LONG 25','pair':'ETHUSDT','amount':'0.2'} # size close 0.05

x = requests.post(url, json = data)

print(x.text)