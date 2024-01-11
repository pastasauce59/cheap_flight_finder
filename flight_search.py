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

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=tequila_config, headers=headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None
        # print(data)

        flight_data = FlightData(
            price = data["price"],
            origin_city = data["route"][0]["cityFrom"],
            origin_airport = data["route"][0]["flyFrom"],
            destination_city = data["route"][0]["cityTo"],
            destination_airport = data["route"][0]["flyTo"],
            depart_date = data["route"][0]["local_departure"].split("T")[0],
            return_date = data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
