import math


class Point:
    def __init__(self, x=0, y=0):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Los valores deben ser números.")
        else : 
            self.x = x
            self.y = y

    def compute_distance(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.length = None
        self.slope = None

    def compute_length(self) -> float:
        self.length = self.start.compute_distance(self.end)
        return self.length

    def compute_slope(self) -> float:      
        if (self.end.x - self.start.x) == 0:
            raise ZeroDivisionError("No se puede dividir por cero.")
        else:
            return  (self.end.y - self.start.y) / (self.end.x - self.start.x)
        
    def compute_horizontal_cross(self) -> bool:
        return (self.start.y > 0 and self.end.y < 0) or (self.start.y < 0 and self.end.y > 0)

    def compute_vertical_cross(self) -> bool:
        return (self.start.x > 0 and self.end.x < 0) or (self.start.x < 0 and self.end.x > 0)


class Shape:
    def __init__(self, vertices: list[Point], edges: list[Line] = None):
        self._vertices = vertices
        self._edges = []
        self._is_regular = False
        self._inner_angles = []

        if edges is None:
            for i in range(len(vertices)):
                start = vertices[i]
                end = vertices[(i + 1) % len(vertices)]
                self._edges.append(Line(start, end))
        else:
            self._edges = edges

    def get_vertices(self):
        return self._vertices

    def get_edges(self):
        return self._edges

    def get_inner_angles(self):
        return self._inner_angles

    def get_is_regular(self):
        return self._is_regular

    def set_vertices(self, new_vertices):
        if new_vertices:
            self._vertices = new_vertices

    def set_edges(self, new_edges):
        if new_edges:
            self._edges = new_edges

    def set_inner_angles(self, new_inner_angles):
        if new_inner_angles:
            self._inner_angles = new_inner_angles
