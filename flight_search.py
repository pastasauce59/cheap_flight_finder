import requests
from keys import *
from flight_data import FlightData

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
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        tequila_config = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "curr": "USD",
            "max_stopovers": 0
        }
