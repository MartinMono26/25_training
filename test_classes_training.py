from classes_training import Cylinder

class TestCylinder:

    def test_get_volume(self):
        c1 = Cylinder(
            name='c1',
            height=2,
            diameter=4
        )
        v = c1.get_volume()
        assert(v==25.132741228718345)

    def test_tata(self):
        assert(False)
