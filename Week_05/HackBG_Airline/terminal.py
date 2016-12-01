class Terminal:
    def __init__(self, number, max_flights):
        self.number = number
        self.max_flights = max_flights
        self.flights = []

    def __str__(self):
        return "Terminal {0}".format(self.number)

    def __repr__(self):
        return self.__str__()

    def get_terminal_flights(self):
        return self.flights

    def get_terminal_flights_on(self, date):
        return [fl for fl in self.flights if fl.start_time.date == date]

    def terminal_flights_to_dest(self, destination):
        return [fl for fl in self.flights if fl.to_dest == destination]

    def passengers_from_terminal(terminal):
        pass
