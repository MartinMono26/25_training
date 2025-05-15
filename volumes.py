from datetime import datetime
import math

class Volume:
    nb_volumes=0
    def __init__(self, name: str):
        self.name = name
        self.date_creation = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

class Cylinder(Volume):
    nb_cylinder=0
    def __init__(self, name:str, diameter:float, height:int):
        super().__init__(
            name=name
        )
        Cylinder.nb_cylinder+=1
        self.diameter = diameter
        self.height = height

    def get_volume(self) -> float:
        return self.get_cylinder_volume(
            height=self.height,
            diameter=self.diameter)

    @staticmethod
    def get_cylinder_volume(height:float, diameter:float)-> float:
        return math.pi * (0.5 * diameter) ** 2 * height

    @classmethod
    def how_many_cylinders(cls):
        return cls.nb_cylinder

    @classmethod
    def depuis_chaine(cls, chaine):
        name, height, diameter = chaine.split("-")
        return cls(name, height, diameter)
