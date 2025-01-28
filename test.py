import unittest
from main import check, divide_new
from main import add, subtract, multiply, divide

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertNotEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)

class TestCheck(unittest.TestCase):
    def testchek(self):
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertTrue(check(220))

        self.assertFalse(check(1))
        self.assertFalse(check(3))
        self.assertFalse(check(57))


# -----------DZ--------------------
    def test_divide_positive_numbers(self):
        self.assertEqual(divide_new(10, 3), (3, 1))  # 10 // 3 = 3, 10 % 3 = 1

    def test_divide_negative_numbers(self):
        self.assertEqual(divide_new(-10, 3), (-4, 2))  # -10 // 3 = -4, -10 % 3 = 2

    def test_divide_by_negative(self):
        self.assertEqual(divide_new(10, -3), (-4, -2))  # 10 // -3 = -4, 10 % -3 = -2

    def test_divide_zero_dividend(self):
        self.assertEqual(divide_new(0, 5), (0, 0))  # 0 // 5 = 0, 0 % 5 = 0

    def test_divide_by_one(self):
        self.assertEqual(divide_new(7, 1), (7, 0))  # 7 // 1 = 7, 7 % 1 = 0

    def test_divide_by_negative_one(self):
        self.assertEqual(divide_new(7, -1), (-7, 0))  # 7 // -1 = -7, 7 % -1 = 0

    def test_divide_large_numbers(self):
        self.assertEqual(divide_new(1000000, 999), (1001, 1))  # 1000000 // 999 = 1001, 1000000 % 999 = 1

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(15, 0)

if __name__ == '__main__':
		unittest.main()