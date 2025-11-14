import unittest
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    def test_area_zero(self):
       self.assertEqual(area(10,0), 0)
       self.assertEqual(area(0,10), 0)
       self.assertEqual(area(0,0), 0)
    
    def test_area_positive_integers(self):
        self.assertEqual(area(1,2), 2)
        self.assertEqual(area(4,5), 20)
        self.assertEqual(area(10,20), 200)
        self.assertEqual(area(67,1), 67)
        self.assertEqual(area(56,78), 4368)
        self.assertEqual(area(100,100), 10000)
    
    def test_area_positive_floats(self):
        self.assertAlmostEqual(area(1.1,1.1), 1.21)
        self.assertAlmostEqual(area(0.1,0.2), 0.02)
        self.assertAlmostEqual(area(4.0,2.5), 10.0)
        self.assertAlmostEqual(area(0.18,2.576), 0.46368)
        self.assertAlmostEqual(area(4.00000,2.500000), 10.0)
        self.assertAlmostEqual(area(67.67,67.78), 4586.6726)
        
    def test_area_negative_integers(self):
        self.assertFalse(area(-1,-2))
        self.assertFalse(area(-4,5))
        self.assertFalse(area(10,-20))
        self.assertFalse(area(-67,-1))
        self.assertFalse(area(-56,78))
        self.assertFalse(area(100,-100))

    def test_area_negative_floats(self):
        self.assertFalse(area(-1.1, -1.1))
        self.assertFalse(area(-0.1, 0.2))
        self.assertFalse(area(4.0, -2.5))
        self.assertFalse(area(-0.18, -2.576))
        self.assertFalse(area(-4.00000, 2.500000))
        self.assertFalse(area(-67.67, -67.78))

    def test_area_different_types_of_numbers(self):
        self.assertAlmostEqual(area(1, 1.1), 1.1)
        self.assertAlmostEqual(area(0.1, 5), 0.5)
        self.assertFalse(area(-10, -2.5))
        self.assertFalse(area(-0.18, 1))   
        self.assertFalse(area(4.00000, -78))

    def test_area_string_error(self):
        with self.assertRaises(TypeError): area("1",2)
        with self.assertRaises(TypeError): area(4,"5")
        with self.assertRaises(TypeError): area("hello","?")
        with self.assertRaises(TypeError): area("67","67")

    def test_area_other_invalid_types(self):
        with self.assertRaises(TypeError): area([1,2],4)
        with self.assertRaises(TypeError): area(5,[0.02])
        with self.assertRaises(TypeError): area(None,67)
        with self.assertRaises(TypeError): area(148,None)
        
    def test_perimeter_zero(self):
       self.assertEqual(perimeter(10,0), 20)
       self.assertEqual(perimeter(0,10), 20)
       self.assertEqual(perimeter(0,0), 0)
    
    def test_perineter_positive_integers(self):
        self.assertEqual(perimeter(1,2), 6)
        self.assertEqual(perimeter(4,5), 18)
        self.assertEqual(perimeter(10,20), 60)
        self.assertEqual(perimeter(67,1), 136)
        self.assertEqual(perimeter(56,78), 268)
        self.assertEqual(perimeter(100,100), 400)

    def test_perimeter_positive_floats(self):
        self.assertAlmostEqual(perimeter(1.1,1.1), 4.4)
        self.assertAlmostEqual(perimeter(0.1,0.2), 0.6)
        self.assertAlmostEqual(perimeter(4.0,2.5), 13.0)
        self.assertAlmostEqual(perimeter(0.18,2.576), 5.512)
        self.assertAlmostEqual(perimeter(4.00000,2.500000), 13.0)
        self.assertAlmostEqual(perimeter(67.67,67.78), 270.9)

    def test_perimeter_negative_integers(self):
        self.assertFalse(perimeter(-1,-2))
        self.assertFalse(perimeter(-4,5))
        self.assertFalse(perimeter(10,-20))
        self.assertFalse(perimeter(-67,-1))
        self.assertFalse(perimeter(-56,78))
        self.assertFalse(perimeter(100,-100))
    
    def test_perimeter_negative_floats(self):
        self.assertFalse(perimeter(-1.1, -1.1))
        self.assertFalse(perimeter(-0.1, 0.2))
        self.assertFalse(perimeter(4.0, -2.5))
        self.assertFalse(perimeter(-0.18, -2.576))
        self.assertFalse(perimeter(-4.00000, 2.500000))
        self.assertFalse(perimeter(-67.67, -67.78))

    def test_perimeter_different_types_of_number(self):
        self.assertAlmostEqual(perimeter(1, 1.1), 4.2)
        self.assertAlmostEqual(perimeter(0.1, 5), 10.2)
        self.assertFalse(perimeter(-10, -2.5))
        self.assertFalse(perimeter(-0.18, 1))   
        self.assertFalse(perimeter(4.00000, -78))

    def test_perimeter_string_error(self):
        with self.assertRaises(TypeError): perimeter("1",2)
        with self.assertRaises(TypeError): perimeter(4,"5")
        with self.assertRaises(TypeError): perimeter("hello","?")
        with self.assertRaises(TypeError): perimeter("67","67")

    def test_perimeter_other_invalid_types(self):
        with self.assertRaises(TypeError): perimeter([1,2],4)
        with self.assertRaises(TypeError): perimeter(5,[0.02])
        with self.assertRaises(TypeError): perimeter(None,67)
        with self.assertRaises(TypeError): perimeter(148,None)