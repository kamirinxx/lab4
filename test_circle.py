import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(10)
        self.assertAlmostEqual(res, math.pi * 100, places=2)

    def test_area_zero(self):
        res = area (0)
        self.assertEqual(res, 0) 

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_area_type_error(self):
        with self.assertRaises(TypeError):
            area("10")

    def test_perimeter_positive(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 20 * math.pi, places = 2)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_perimeter_type_error(self):
        with self.assertRaises(TypeError):
            perimeter("10")

