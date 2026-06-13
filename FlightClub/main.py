import requests_cache
from datetime import datetime,timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import find_cheapest_flight
from pprint import pprint

#------cashing json data---------#
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

#---------setting dates--------#
tomorrow = datetime.now() + timedelta(days=1)
return_date = tomorrow + timedelta(days=7)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

#----------sheet data-----------#
data_manager = DataManager()
sheet_data = data_manager.price_data
pprint(sheet_data)

#---------customer emails---------#
customer_data = data_manager.get_customer_emails()
customer_email_list = [row["whatIsYourEmail?"] for row in customer_data]

#------------flight search/origin city-----------#
flight_search = FlightSearch()
ORIGIN_CITY_IATA = "JFK"


#-------------flight search for every desired city---------------#
for destination in sheet_data:

    #------------direct flight search------------#
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=return_date
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=return_date.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: USD {cheapest_flight.price}")

#-------------indirect flight search-----------#
    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=return_date,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights, return_date=return_date.strftime("%Y-%m-%d"))
        pprint(f"Cheapest indirect flight to {destination['city']}: USD {cheapest_flight.price}")

#------------------comparing the cheapest prices to desired price-------------------#
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price)
        #-------------updating the cheapest price and sending notifications-------------#
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only USD {cheapest_flight.price} to fly direct " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only GBP {cheapest_flight.price} to fly " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"with {cheapest_flight.stops} stop(s) " \
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."

        notification_manager = NotificationManager()
        notification_manager.send_whatsapp(message)
        notification_manager.send_email(customer_email_list,message)





















