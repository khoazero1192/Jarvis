# Main app
import requests
import json
import pandas as pd
import schedule
import time

from jarvis import Jarvis

HEADERS = {'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
           'x-rapidapi-key': "cecf414141msh96489e04be93bcfp177721jsn55924ff9efaa"}
QUERRY_STRING = {"region": "US", "start": "0", "lang": "en-US", "count": "6"}


class Main(object):
    def __init__(self):
        data = json.load(open("creds.json", 'r'))
        self.jarvis = Jarvis(data['id'], data['password'], '3181465165315259')

    def get_movers(self):
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-movers"
        resp = requests.request("GET", url, headers=HEADERS, params=QUERRY_STRING).json()
        data = resp["finance"]["result"][0]["quotes"]
        string = "TOP movers: \n"
        for item in data:
            string += "%s\n" % item["symbol"]
        print("Sending notification about top movers")
        self.jarvis.send_message(string)


# main thread
main = Main()
schedule.every().day.at("06:00").do(main.get_movers)
while True:
    schedule.run_pending()
    time.sleep(1)