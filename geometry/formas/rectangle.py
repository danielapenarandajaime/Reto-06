import math

from base.shape import Point, Line, Shape



class Rectangle(Shape):
    def __init__(self, vertices: list[Point], edges: list[Line] = None):
        super().__init__(vertices, edges)

        if len(self._vertices) != 4:
            # Definition of Rectangle
            raise ValueError("A rectangle must have exactly 4 vertices")

        self.line1 = self._edges[0]
        self.line2 = self._edges[1]
        self.line3 = self._edges[2]
        self.line4 = self._edges[3]

        len1 = self.line1.compute_length()
        len2 = self.line2.compute_length()
        len3 = self.line3.compute_length()
        len4 = self.line4.compute_length()

        if not (math.isclose(len1, len3) and math.isclose(len2, len4)):
            raise ValueError("Opposite sides must be equal in a rectangle")

        self.width = min(len1, len2)
        self.height = max(len1, len2)

        x_coords = [p.x for p in self._vertices]
        y_coords = [p.y for p in self._vertices]
        self.center = Point(sum(x_coords) / 4, sum(y_coords) / 4)

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * self.width + 2 * self.height

    def compute_interference_point(self, point: Point) -> str:
        x_right = self.center.x + (self.width / 2)
        x_left = self.center.x - (self.width / 2)
        y_top = self.center.y + (self.height / 2)
        y_bottom = self.center.y - (self.height / 2)

        if (x_left < point.x < x_right and 
            y_bottom < point.y < y_top):
            return "The point is inside the rectangle."
        return "The point is outside the rectangle."

    def compute_inner_angles(self):
        return [90, 90, 90, 90]


class Square(Rectangle):
    def __init__(self, vertices: list[Point], edges: list[Line] = None):
        super().__init__(vertices, edges)

        lengths = [edge.compute_length() for edge in self._edges]
        if not all(math.isclose(lengths[0], l) for l in lengths):
            # Definition of Square
            raise ValueError("A square must have all sides of equal length")

        self._is_regular = True