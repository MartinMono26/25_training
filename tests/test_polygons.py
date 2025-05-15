import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from polygons import Square

class TestPolygon:

    def test_compute_area(self):
        s=Square( name = 's1', side_length_mm = 5)
        s.compute_area()
        assert (s.area==25)

    def test_pif(self):
        assert (True)

    def test_paf(self):
        assert (True)