"""
Stwórz klasę Kwadrat
"""


class Rectangle:
    """
    def __init__(self, w, h):
        self.width = w
        self.height = h

    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_circuit(self):
        return 2 * self.width + 2 * self.height


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)


if __name__ == "__main__":
    rectangle = Rectangle(2, 3)
    print(rectangle.calculate_area())
    print(rectangle.calculate_circuit())

    square = Square(2)
    print(square.calculate_area())
    print(square.calculate_circuit())

    print(isinstance(rectangle, Rectangle))
    print(isinstance(rectangle, Square))

    print(isinstance(square, Rectangle))
    print(isinstance(square, Square))
