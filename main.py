from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
# print(len(sheet_data))

for i in range(0, len(sheet_data)):
    if sheet_data[i]["iataCode"] == "":
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        sheet_data[i]["iataCode"] = flight_search.get_destination_code(sheet_data[i]["city"])
        # print(f"Sheet Data: \n {sheet_data}" )
        
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

ORIGIN_CITY_IATA = "JFK"
tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_mons_from_now = (datetime.now() + timedelta((6 * 30))).strftime("%d/%m/%Y")

# print(sheet_data)

for city in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        city["iataCode"],
        tomorrow,
        six_mons_from_now
    )

    if flight.price < city["lowestPrice"]:
        notification_manager.send_message(message=
        f"Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport} from {flight.depart_date} to {flight.return_date}!")

