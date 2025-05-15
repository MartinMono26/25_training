import networkx
import datetime


class Vehicle:
    nb_vehicle = 0


class Car(Vehicle):
    def __init__(self):
        Vehicle.nb_vehicle += 1