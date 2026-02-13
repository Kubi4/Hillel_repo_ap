from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimeter(self):
        return 4 * self.__side

class Triangle(Figure):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return (3 ** 0.5 / 4) * self.__side ** 2

    def perimeter(self):
        return 3 * self.__side

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return 3.1416 * self.__radius ** 2

    def perimeter(self):
        return 2 * 3.1416 * self.__radius

figures = [Square(5), Triangle(3), Circle(2), Square(10), Triangle(6), Circle(5)]

for figure in figures:
    print(f"{figure.__class__.__name__}:")
    print(f"  Площа: {figure.area():.2f}")
    print(f"  Периметр: {figure.perimeter():.2f}")