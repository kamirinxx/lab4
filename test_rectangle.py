import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_zero(self):
        res = area (10, 0)
        self.assertEqual(res, 0) 

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5, 10)

    def test_area_type_error(self):
        with self.assertRaises(TypeError):
            area("10", 10)

    def test_perimeter_positive(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_zero(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 10)

    def test_perimeter_type_error(self):
        with self.assertRaises(TypeError):
            perimeter("10", 10)

