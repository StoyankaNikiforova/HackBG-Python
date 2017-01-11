from jsonable import Jsonable
from xmlable import Xmlable


class Panda(Jsonable, Xmlable):
    def __init__(self, name):
        self.name = name

        
