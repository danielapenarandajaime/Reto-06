import math

from base.shape import Point, Line, Shape



class Triangle(Shape):
    def __init__(self, vertices: list[Point], edges: list[Line] = None):
        if len(vertices) != 3:
            # Definition of triangle
            raise ValueError("A triangle must have exactly 3 vertices")

        super().__init__(vertices, edges)

        self.line1 = self._edges[0]
        self.line2 = self._edges[1]
        self.line3 = self._edges[2]

        self.len1 = self.line1.compute_length()
        self.len2 = self.line2.compute_length()
        self.len3 = self.line3.compute_length()

        self._is_regular = math.isclose(self.len1, self.len2) and math.isclose(self.len2, self.len3)
        self._inner_angles = self.compute_inner_angles()

    def compute_inner_angles(self):
        angle_a = math.degrees(math.acos(
            (self.len3**2 + self.len1**2 - self.len2**2) / 
            (2 * self.len3 * self.len1)
        ))
        angle_b = math.degrees(math.acos(
            (self.len2**2 + self.len1**2 - self.len3**2) / 
            (2 * self.len2 * self.len1)
        ))
        angle_c = 180 - angle_a - angle_b

        return [angle_a, angle_b, angle_c]

    def compute_area(self):
        s = (self.len1 + self.len2 + self.len3) / 2
        return math.sqrt(s * (s - self.len1) * (s - self.len2) * (s - self.len3))

    def compute_perimeter(self):
        return self.len1 + self.len2 + self.len3


class Isosceles(Triangle):
    def __init__(self, vertices: list[Point], edges: list[Line] = None):
        super().__init__(vertices, edges)

        lengths = [edge.compute_length() for edge in self._edges]
        unique_lengths = len(set(round(l, 6) for l in lengths))
        if unique_lengths != 2:
            # Definition of isosceles triangle
            raise ValueError("An isosceles triangle must have exactly two equal sides")


class Equilateral(Triangle):
    def __init__(self, vertices: list[Point], edges: list[Line] = None):
        super().__init__(vertices, edges)

        lengths = [edge.compute_length() for edge in self._edges]
        if not all(math.isclose(lengths[0], l) for l in lengths):
            # Definition of equilateral triangle
            raise ValueError("An equilateral triangle must have all sides equal") 


class Scalene(Triangle):
    def __init__(self, vertices: list[Point], edges: list[Line] = None):
        super().__init__(vertices, edges)

        lengths = [edge.compute_length() for edge in self._edges]
        if len(set(round(l, 6) for l in lengths)) != 3:
            # Definition of scalene triangle
            raise ValueError("A scalene triangle must have all sides different")


class TriRectangle(Triangle):
    def __init__(self, vertices: list[Point], edges: list[Line] = None):
        super().__init__(vertices, edges)

        angles = self.compute_inner_angles()
        if not any(math.isclose(angle, 90) for angle in angles):
            # Definition of TriRectangle triangle
            raise ValueError("A right triangle must have one 90-degree angle")