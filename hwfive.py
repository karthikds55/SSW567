import unittest
import datetime



def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        if (a*2 + b*2 == c*2) or (a*2 + c*2 == b*2) or (b*2 + c*2 == a*2):
            return "Isosceles and Right"
        return "Isosceles"
    if a != b and b != c and a != c:
        if a*2 + b*2 == c*2 or a*2 + c*2 == b*2 or b*2 + c*2 == a*2:
            return "Scalene and Right"
        return "Scalene"

class TestTriangleClassification(unittest.TestCase):
    def test_triangle(self):
        # self.assertEqual(classify_triangle(1, 1, 1), "Isosceles")
        self.assertEqual(classify_triangle(3, 3, 4), "Isosceles")
        self.assertEqual(classify_triangle(8, 14, 17), "Scalene")
        self.assertEqual(classify_triangle(30, 30, 30), "Equilateral")


if __name__ == "__main__":
    # classify_triangle(2,5,9)
    # classify_triangle(3,3,3)
    unittest.main()
