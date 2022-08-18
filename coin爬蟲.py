import time
import requests
import json

while True:
    # Defining Binance API URL

    key = "https://api.binance.com/api/v3/ticker/price?symbol="

    # Making list for multiple crypto's

    currencies = ["BTCUSDT", "ETHUSDT", "ADAUSDT"]

    j = 0

    # running loop to print all crypto prices

    for i in currencies:

            # completing API for request

        url = key+currencies[j]

        data = requests.get(url)

        data = data.json()

        j = j+1


    # 發送到 line notify
        headers = {
            "Authorization": "Bearer " + "line權杖需替換",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        params = {'message' : f"{data['symbol']} $ {float(data['price'])}"}

        r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=params)
        print(params)
    time.sleep(30)