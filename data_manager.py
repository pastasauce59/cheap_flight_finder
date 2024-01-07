import requests
from pprint import pprint
from keys import *

sheety_headers = {
            "Authorization": SHEETY_TOKEN
        }

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data)
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", headers=sheety_headers, json=new_data)
            print(response.text)
