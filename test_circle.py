import math
import unittest
from circle import area, perimeter

class TestCircle(unittest.TestCase):
    def test_area_zero(self):
       self.assertEqual(area(0), 0)
    
    def test_area_positive_integers(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(5), 25 * math.pi)
        self.assertAlmostEqual(area(10), 100 * math.pi)
        self.assertAlmostEqual(area(67), 4489 * math.pi)
        self.assertAlmostEqual(area(56), 3136 * math.pi)
        self.assertAlmostEqual(area(100), 10000 * math.pi)

    def test_area_positive_floats(self):
        self.assertAlmostEqual(area(1.1), 1.21 * math.pi)
        self.assertAlmostEqual(area(0.1), 0.01 * math.pi)
        self.assertAlmostEqual(area(4.0), 16.0 * math.pi)
        self.assertAlmostEqual(area(2.576), 6.635776 * math.pi)
        self.assertAlmostEqual(area(2.500000), 6.25 * math.pi)
        self.assertAlmostEqual(area(67.67), 4579.2289 * math.pi)
        
    def test_area_negative_integers(self):
        self.assertFalse(area(-2))
        self.assertFalse(area(-4))
        self.assertFalse(area(-20))
        self.assertFalse(area(-1))
        self.assertFalse(area(-56))
        self.assertFalse(area(-100))

    def test_area_negative_floats(self):
        self.assertFalse(area(-1.1))
        self.assertFalse(area(-0.1))
        self.assertFalse(area(-2.5))
        self.assertFalse(area(-0.18))
        self.assertFalse(area(-4.00000))
        self.assertFalse(area(-67.67))

    def test_area_string_error(self):
        with self.assertRaises(TypeError): area("1")
        with self.assertRaises(TypeError): area("hello")
        with self.assertRaises(TypeError): area("^")
        with self.assertRaises(TypeError): area("не")
        with self.assertRaises(TypeError): area("[}]")

    def test_area_other_invalid_types(self):
        with self.assertRaises(TypeError): area([1,2])
        with self.assertRaises(TypeError): area(None)
        
    def test_perimeter_zero(self):
       self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_positive_integers(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(5), 10 * math.pi)
        self.assertAlmostEqual(perimeter(10), 20 * math.pi)
        self.assertAlmostEqual(perimeter(67), 134 * math.pi)
        self.assertAlmostEqual(perimeter(56), 112 * math.pi)
        self.assertAlmostEqual(perimeter(100), 200 * math.pi)

    def test_perimeter_positive_floats(self):
        self.assertAlmostEqual(perimeter(1.1), 2.2 * math.pi)
        self.assertAlmostEqual(perimeter(0.1), 0.2 * math.pi)
        self.assertAlmostEqual(perimeter(4.0), 8.0 * math.pi)
        self.assertAlmostEqual(perimeter(2.576), 5.152 * math.pi)
        self.assertAlmostEqual(perimeter(2.500000), 5.0 * math.pi)
        self.assertAlmostEqual(perimeter(67.67), 135.34 * math.pi)
        
    def test_perimeter_negative_integers(self):
        self.assertFalse(perimeter(-2))
        self.assertFalse(perimeter(-4))
        self.assertFalse(perimeter(-20))
        self.assertFalse(perimeter(-1))
        self.assertFalse(perimeter(-56))
        self.assertFalse(perimeter(-100))

    def test_perimeter_negative_floats(self):
        self.assertFalse(perimeter(-1.1))
        self.assertFalse(perimeter(-0.1))
        self.assertFalse(perimeter(-2.5))
        self.assertFalse(perimeter(-0.18))
        self.assertFalse(perimeter(-4.00000))
        self.assertFalse(perimeter(-67.67))

    def test_perimeter_string_error(self):
        with self.assertRaises(TypeError): perimeter("1")
        with self.assertRaises(TypeError): perimeter("hello")
        with self.assertRaises(TypeError): perimeter("^")
        with self.assertRaises(TypeError): perimeter("не")
        with self.assertRaises(TypeError): perimeter("[}]")

    def test_perimeter_other_invalid_types(self):
        with self.assertRaises(TypeError): perimeter([1,2])
        with self.assertRaises(TypeError): perimeter(None)