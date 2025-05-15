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

if __name__ == '__main__':
    c1=Cylinder(
        name='c1',
        height=2,
        diameter=4
    )
    v=c1.get_volume()

    print(f"Volume {v},  type {type(v)} ")

    print(f"As a static method: {Cylinder.get_cylinder_volume(height=3, diameter=7.8452)} ----")

    c2 = Cylinder(
        name='c2',
        height=4.452,
        diameter=8
    )

    print(f"{Cylinder.how_many_cylinders()} cylinders have been created")

    c3=Cylinder.depuis_chaine(chaine="c4-2.5-5.8")


    e=1