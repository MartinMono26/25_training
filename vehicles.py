import networkx
from datetime import datetime

class Vehicle:
    nb_vehicle = 0

class Car(Vehicle):
    def __init__(self, name):
        Vehicle.nb_vehicle += 1
        self.name=name

class Polygon:
  nb_polygon=0

  def __init__(self, name):
    self.name=name
