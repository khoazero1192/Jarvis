# Main app
import requests
import json
import argparse

from jarvis import Jarvis

HEADERS = {'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
           'x-rapidapi-key': "cecf414141msh96489e04be93bcfp177721jsn55924ff9efaa"}
QUERRY_STRING = {"region": "US", "start": "0", "lang": "en-US", "count": "6"}
STOCK_GROUP_ID = "4151234508237032"
TEST_GROUP_ID = "3181465165315259"


class Main(object):
    def __init__(self, gid=TEST_GROUP_ID):
        data = json.load(open("creds.json", 'r'))
        self.jarvis = Jarvis(data['id'], data['password'], gid)

    def get_movers(self):
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-movers"
        resp = requests.request("GET", url, headers=HEADERS, params=QUERRY_STRING).json()
        gainers = resp["finance"]["result"][0]["quotes"]
        string = "TOP Gainers: \n"
        for item in gainers:
            string += "%s\n" % item["symbol"]

        losers = resp["finance"]["result"][1]["quotes"]
        string += "-------------------\n"
        string += "TOP Losers: \n"
        for item in losers:
            string += "%s\n" % item["symbol"]
        print("Sending notification about top movers")
        self.jarvis.send_message(string)


parser = argparse.ArgumentParser(description='What is the group ID')
parser.add_argument('-gid', metavar='group_id',
                    help='an integer for the accumulator')

args = parser.parse_args()
main = Main(args.gid)
main.get_movers()

