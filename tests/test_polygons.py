from polygons import Polygon, Square

class TestPolygon:

    def test_compute_area(self):
        s=Square( name = 's1', side_length_mm = 5)
        s.compute_area()
        assert (s.area==25)
