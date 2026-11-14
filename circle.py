import math

def area(r):
    if not isinstance(r, (int, float)):
        raise TypeError
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r ** 2

def perimeter(r):
    if not isinstance(r, (int, float)):
        raise TypeError
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r