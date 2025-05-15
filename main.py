from src.volumes import Cylinder

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