import requests_cache
from datetime import datetime,timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import find_cheapest_flight
from pprint import pprint

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

tomorrow = datetime.now() + timedelta(days=1)
return_date = tomorrow + timedelta(days=7)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

data_manager = DataManager()
sheet_data = data_manager.data
pprint(sheet_data)

flight_search = FlightSearch()
ORIGIN_CITY_IATA = "LHR"

for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=return_date
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=return_date.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: GBP {cheapest_flight.price}")

    if str(cheapest_flight.price) != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower price flight found to {destination['city']}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        message = f"""Low price alert! Only {cheapest_flight.price}
                      to fly from {ORIGIN_CITY_IATA} to {destination['iataCode']}
                      on {tomorrow} until {return_date}."""

        notification_manager = NotificationManager()
        notification_manager.send_whatsapp(message)





















