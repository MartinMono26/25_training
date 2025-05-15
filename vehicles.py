import networkx
from datetime import datetime


class Polygon:
  nb_polygon=0
class Vehicle:
    nb_vehicle = 0


class Car(Vehicle):
    def __init__(self, name):
        Vehicle.nb_vehicle += 1
        self.name=name
