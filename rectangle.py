def area(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a * b

def perimeter(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return (a + b) * 2
