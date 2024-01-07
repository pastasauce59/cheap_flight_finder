import requests
from pprint import pprint
from keys import *

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheety_headers = {
            "Authorization": SHEETY_TOKEN
        }
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data)
        return self.destination_data

