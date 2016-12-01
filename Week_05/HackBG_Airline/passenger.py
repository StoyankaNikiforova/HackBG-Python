class Passenger:
    def __init__(self, first_name, last_name, flight, age):
        self.first_name = first_name
        self.last_name = last_name
        self.flight = flight
        self.age = age

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name,
                                 self.flight.id_number)

    def __repr__(self):
        return self.__str__()
