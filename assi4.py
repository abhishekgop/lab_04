class Flight:
    def __init__(self, flight_id, origin, destination, price):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def flights_for_city(self, city):
        return [flight for flight in self.flights if flight.origin == city or flight.destination == city]

    def flights_from_city(self, city):
        return [flight for flight in self.flights if flight.origin == city]

    def flights_between_cities(self, city1, city2):
        return [flight for flight in self.flights if (flight.origin == city1 and flight.destination == city2) or
                (flight.origin == city2 and flight.destination == city1)]

def main():
    flight_table = FlightTable()

    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    for data in flight_data:
        flight = Flight(data[0], data[1], data[2], data[3])
        flight_table.add_flight(flight)

    print("Search Options:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter the city: ")
        result = flight_table.flights_for_city(city)
    elif choice == 2:
        city = input("Enter the city: ")
        result = flight_table.flights_from_city(city)
    elif choice == 3:
        city1 = input("Enter the first city: ")
        city2 = input("Enter the second city: ")
        result = flight_table.flights_between_cities(city1, city2)
    else:
        print("Invalid choice")
        return

    if result:
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in result:
            print(f"{flight.flight_id}\t{flight.origin}\t{flight.destination}\t{flight.price}")
    else:
        print("No flights found.")

if __name__ == "__main__":
    main()
