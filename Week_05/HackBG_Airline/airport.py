import json
from objects_generator import Generator


class Airport:
    DATA = Generator(2, 40, 100, 50)

    def __init__(self, DATA):
        # with open(file_name, 'r') as f:
        #     data = json.loads(f.read())
        self.flights = DATA.flights
        self.terminals = DATA.terminals
        self.passengers = DATA.passengers
        self.reservations = DATA.reservations

    def get_flights_for(self, date):
        return [i for i in self.flights if i.start_time == date]

    def get_flights_before(self, date, hour):
        return [i for i in self.flights if i.hour.all_sec < hour.all_sec]

    def get_flight_from(self, destination):
        return [i.id_number for i in self.flights if i.from_dest == destination]

    def get_flight_to(self, destination):
        return [i.id_number for i in self.flights if i.to_dest == destination]

    def get_flight_to(self, destination, date, hour):
        return [i.id_number for i in self.get_flight_to(destination)
                if i.hour == hour and i.date = date]

    def get_flight_from(destination, date, hour):
        pass

    def flights_on_date_lt_hours(date, hours):
        pass

    def flights_within_duration(start_time, end_time):
        pass

    def passengers_to_dest(destination):
        pass

    def get_terminal_flights(self, n):
        return [i.id_number for i in self.flights if i.terminal.number == n]

    def reservations_to_destination(self, destination):
        result = []
        for res in self.reservations:
            for fl in res.flights:
                if fl.to_dest == destination:
                    result.append(res)
        return result

    def passengers_reservations(self, flight):
        result = []
        for res in self.reservations:
            for fl in res.flights:
                if fl.id_number == flight:
                    result.append((res.passenger.first_name,
                                   res.passenger.last_name))
        return result

    def flights_with_passengers(self, size):
        return [fl.passengers_count for fl in self.flights if fl.passengers_count == size]
