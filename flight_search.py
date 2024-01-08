import requests
from keys import *

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"

class FlightSearch:

    def get_destination_code(self, city_name):
        tequila_config = {
            "term": city_name,
            "location_types": "airport"
        }

        tequila_headers = {
             "apikey": TEQUILA_API_KEY,
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=tequila_config, headers=tequila_headers)
        code = response.json()["locations"][0]["code"]
        return code
        # print(code)
