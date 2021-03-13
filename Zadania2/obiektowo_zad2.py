"""
Napisz klasę Prostokąt, konstruowany przy użyciu
szerokości i długości. Dodaj metody w klasie Prostokąt,
które policzą a) obwód b) pole
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_circuit(self):
        return 2 * self.width + 2 * self.height

