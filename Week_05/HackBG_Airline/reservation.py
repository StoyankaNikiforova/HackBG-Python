class Reservation:
    def __init__(self, number, flight, passenger, accepted):
        self.number = number
        self.flight = flight
        self.passenger = passenger
        self.accepted = accepted

    def __str__(self):
        return "Reservation: {0} for flight{1} {2}\n".format(self.number,
                                                             self.flight.id_number,
                                                             self.passenger.last_name)


    def __repr__(self):
        return self.__str__()
