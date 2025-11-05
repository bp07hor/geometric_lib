import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area_zero(self):
       self.assertEqual(area(0), 0)
    
    def test_area_positive_integers(self):
        self.assertEqual(area(1), 1)
        self.assertEqual(area(5), 25)
        self.assertEqual(area(10), 100)
        self.assertEqual(area(67), 4489)
        self.assertEqual(area(56), 3136)
        self.assertEqual(area(100), 10000)

    def test_area_positive_floats(self):
        self.assertAlmostEqual(area(1.1), 1.21)
        self.assertAlmostEqual(area(0.1), 0.01)
        self.assertAlmostEqual(area(4.0), 16.0)
        self.assertAlmostEqual(area(2.576), 6.635776)
        self.assertAlmostEqual(area(2.500000), 6.25)
        self.assertAlmostEqual(area(67.67), 4579.2289)
        
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
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(10), 40)
        self.assertEqual(perimeter(67), 268)
        self.assertEqual(perimeter(56), 224)
        self.assertEqual(perimeter(100), 400)

    def test_perimeter_positive_floats(self):
        self.assertAlmostEqual(perimeter(1.1), 4.4)
        self.assertAlmostEqual(perimeter(0.1), 0.4)
        self.assertAlmostEqual(perimeter(4.0), 16.0)
        self.assertAlmostEqual(perimeter(2.576), 10.304)
        self.assertAlmostEqual(perimeter(2.500000), 10.0)
        self.assertAlmostEqual(perimeter(67.67), 270.68)
        
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