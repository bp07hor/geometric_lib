import unittest
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area_zero(self):
       self.assertEqual(area(10,0), 0)
       self.assertEqual(area(0,10), 0)
       self.assertEqual(area(0,0), 0)
    
    def test_area_positive_integers(self):
        self.assertEqual(area(1,2), 1)
        self.assertEqual(area(4,5), 10)
        self.assertEqual(area(10,20), 100)
        self.assertAlmostEqual(area(67,1), 33.5)
        self.assertEqual(area(56,78), 2184)
        self.assertEqual(area(100,100), 5000)
    
    def test_area_positive_floats(self):
        self.assertAlmostEqual(area(1.1,1.1), 0.605)
        self.assertAlmostEqual(area(0.1,0.2), 0.01)
        self.assertAlmostEqual(area(4.0,2.5), 5.0)
        self.assertAlmostEqual(area(0.18,2.576), 0.23184)
        self.assertAlmostEqual(area(4.00000,2.500000), 5.0)
        self.assertAlmostEqual(area(67.67,67.78), 2293.3363)
        
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
        self.assertAlmostEqual(area(1, 1.1), 0.55)
        self.assertAlmostEqual(area(0.1, 5), 0.25)
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
       self.assertEqual(perimeter(10,0,0), 10)
       self.assertEqual(perimeter(0,10,0), 10)
       self.assertEqual(perimeter(0,0,10), 10)
       self.assertEqual(perimeter(0,0,0), 0)
    
    def test_perineter_positive_integers(self):
        self.assertEqual(perimeter(1,2,3), 6)
        self.assertEqual(perimeter(4,5,6), 15)
        self.assertEqual(perimeter(10,20,30), 60)
        self.assertEqual(perimeter(67,1,56), 124)
        self.assertEqual(perimeter(56,78,90), 224)
        self.assertEqual(perimeter(100,100,100), 300)

    def test_perimeter_positive_floats(self):
        self.assertAlmostEqual(perimeter(1.1,1.1,1.1), 3.3)
        self.assertAlmostEqual(perimeter(0.1,0.2,0.3), 0.6)
        self.assertAlmostEqual(perimeter(4.0,2.5,6.5), 13.0)
        self.assertAlmostEqual(perimeter(0.18,2.576,3.390), 6.146)
        self.assertAlmostEqual(perimeter(4.00000,2.500000, 6.500000), 13.0)
        self.assertAlmostEqual(perimeter(67.67,67.78,67.89), 203.34)

    def test_perimeter_negative_integers(self):
        self.assertFalse(perimeter(-1,-2,-3))
        self.assertFalse(perimeter(-4,5,-6))
        self.assertFalse(perimeter(10,-20,30))
        self.assertFalse(perimeter(-67,-1,56))
        self.assertFalse(perimeter(-56,78,-44))
        self.assertFalse(perimeter(100,-100,100))
    
    def test_perimeter_negative_floats(self):
        self.assertFalse(perimeter(-1.1, -1.1, -1.1))
        self.assertFalse(perimeter(-0.1, 0.2, 0.3))
        self.assertFalse(perimeter(4.0, -2.5, 7.0))
        self.assertFalse(perimeter(-0.18, -2.576, -78.90))
        self.assertFalse(perimeter(-4.00000, 2.500000, -6.500000))
        self.assertFalse(perimeter(-67.67, -67.78, 67.89))

    def test_perimeter_different_types_of_number(self):
        self.assertAlmostEqual(perimeter(1, 1.1, 2.1), 4.2)
        self.assertAlmostEqual(perimeter(0.1, 5, 5.1), 10.2)
        self.assertFalse(perimeter(-10, -2.5, 45))
        self.assertFalse(perimeter(-0.18, 1, 0.8900000))   
        self.assertFalse(perimeter(4.00000, -78, 54))

    def test_perimeter_string_error(self):
        with self.assertRaises(TypeError): perimeter("1",2, "54")
        with self.assertRaises(TypeError): perimeter(4,"5", 6)
        with self.assertRaises(TypeError): perimeter("hello","?", "{{{}}}")
        with self.assertRaises(TypeError): perimeter("67","67", "67")

    def test_perimeter_other_invalid_types(self):
        with self.assertRaises(TypeError): perimeter([1,2],4, 7.6)
        with self.assertRaises(TypeError): perimeter(5,[0.02], 0.9)
        with self.assertRaises(TypeError): perimeter(None,67, 43.78)
        with self.assertRaises(TypeError): perimeter(148,None, 21.9584375)