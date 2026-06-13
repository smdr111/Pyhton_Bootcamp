class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,price,origin_airport,destination_airport,out_date,return_date,stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data, return_date):
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    # Combine best_flights and other_flights into one list
    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    # Keep only flights that actually have a price.
    priced_flights = [flight for flight in all_flights if "price" in flight]
    if not priced_flights:
        print("--- No price available for any flight. ---")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    # Pick the flight with the lowest price.
    cheapest = min(priced_flights, key=lambda flight: flight["price"])

    lowest_price = cheapest["price"]
    origin = cheapest["flights"][0]["departure_airport"]["id"]
    destination = cheapest["flights"][-1]["arrival_airport"]["id"]
    out_date = cheapest["flights"][0]["departure_airport"]["time"].split(" ")[0]
    nr_stops = len(cheapest["flights"]) - 1

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)
    print(f"Lowest price to {destination} is USD {lowest_price}")

    return cheapest_flight



