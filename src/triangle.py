import math

from src.rectangle import Figure


class Triangle(Figure):

    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.check_params(side_a, side_b, side_c)
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle {side_a} x {side_b} x {side_c}"

    def check_params(self, side_a, side_b, side_c):
        if (side_a <= 0 or side_b <= 0 or side_c <= 0
                or side_a + side_b < side_c
                or side_a + side_c < side_b
                or side_b + side_c < side_a):
            raise ValueError("Can't create Triangle")

    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        area_tr = math.sqrt(p *
                            (p - self.side_a) *
                            (p - self.side_b) *
                            (p - self.side_c))
        return round(area_tr, 1)

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
