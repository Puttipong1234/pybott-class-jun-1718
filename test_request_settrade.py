#จำลองสัญญาณ
import requests

url = 'http://127.0.0.1:5000/settrade/spot'
data = {'action': 'OPEN LONG','pair':'GULF','amount':'1000'} # size close 0.05

x = requests.post(url, json = data)

print(x.text)