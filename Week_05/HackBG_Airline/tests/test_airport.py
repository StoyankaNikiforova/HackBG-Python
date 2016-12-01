import unittest
from airport import Airport


class testAirport(unittest.TestCase):
    def setUp(self):
        self.airport = Airport()

    def test_get_flights_for(self):
        self.assertListEqual(self.airport.get_flights_for(self.airport,(11. 12. 2012)), )

    def test_get_flights_before(self):
        pass

    def test_get_flight_from(self):
        pass

    def test_get_flight_to(self):
        pass

    def test_get_terminal_flights(self):
        pass

    def test_get_terminal_flights_on(sef):

            pass

    def test_reservations_to_destination(self):
        pass
