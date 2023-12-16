import unittest
from triangle_func import IncorrectTriangleSides, get_triangle_type



class TestGetTriangleType(unittest.TestCase):

    def test_positive_cases(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")
        self.assertEqual(get_triangle_type(5, 5, 5), "equilateral")
        self.assertEqual(get_triangle_type(5, 5, 7), "isosceles")

    def test_negative_cases(self):
        self.assertRaises(IncorrectTriangleSides, get_triangle_type, 0, 4, 5)
        self.assertRaises(IncorrectTriangleSides, get_triangle_type, 3, 4, 8)
        self.assertRaises(IncorrectTriangleSides, get_triangle_type, -1, 2, 3)

if __name__ == '__main__':
    unittest.main()