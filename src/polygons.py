class Polygon:
    nb_polygon=0

    def __init__(self, name):
        self.name=name
        self.shape=None

class Square(Polygon):
    def __init__(self, name:str='no_name', side_length_mm=10):
        super().__init__(name=name)
        self.area = None
        self.shape="square"
        self.side_length_mm=side_length_mm

    @staticmethod
    def area_of_square(side_length_mm:float):
        return side_length_mm**2

    def compute_area(self):
        self.area=Square.area_of_square(self.side_length_mm)

