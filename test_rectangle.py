import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
        
    def test_perimeter_positive(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

