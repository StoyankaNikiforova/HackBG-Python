from date import Date
from terminal import Terminal


class Flight:
    def __init__(self, id_number, start_time, end_time, passengers, max_passengers,
                 from_dest, to_dest, terminal, declined):
        self.id_number = id_number
        self.start_time = start_time
        self.end_time = end_time
        self.passengers_count = passengers
        self.passengers = []
        self.max_passengers = max_passengers
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.terminal = terminal
        self.declined = declined

    def passengers_under_18(self):
        return len([x for x in self.passengers if x.age < 18])

    def flight_duration():
        return end_time - start_time

    def flight_empty_seats():
        return max_passengers - passengers

    def __str__(self):
        return """  Flight{0} from {1} to {2}
    Depart at {3} on {4}
    with {5} from {6} passengers
    Arrived at {7}\n\n""".format(
                    self.id_number, self.from_dest, self.to_dest, self.start_time,
                    self.terminal, self.passengers_count, self.max_passengers,
                    self.end_time)

    def __repr__(self):
        return self.__str__()
