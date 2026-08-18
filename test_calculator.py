import math
import unittest

from calculator import add, cos, divide, mod, multiply, power, sin, sqrt, subtract


class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(add(-1, 1), 0)

    def test_zero_and_positive_number(self):
        self.assertEqual(add(0, 3), 3)


class TestSubtract(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_result_is_negative(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_zero_minus_positive_number(self):
        self.assertEqual(subtract(0, 3), -3)


class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(multiply(-2, 3), -6)

    def test_multiplication_by_zero(self):
        self.assertEqual(multiply(7, 0), 0)


class TestDivide(unittest.TestCase):
    def test_exact_division(self):
        self.assertEqual(divide(10, 2), 5)

    def test_non_integer_result(self):
        self.assertEqual(divide(1, 4), 0.25)

    def test_negative_divided_by_positive(self):
        self.assertEqual(divide(-6, 2), -3)

    def test_division_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


class TestPower(unittest.TestCase):
    def test_power_with_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_with_zero_exponent(self):
        self.assertEqual(power(2, 0), 1)

    def test_power_with_negative_exponent(self):
        self.assertEqual(power(2, -1), 0.5)


class TestSqrt(unittest.TestCase):
    def test_perfect_square(self):
        self.assertEqual(sqrt(16), 4)

    def test_non_perfect_square(self):
        self.assertAlmostEqual(sqrt(2), 1.414, places=3)

    def test_square_root_of_zero(self):
        self.assertEqual(sqrt(0), 0)

    def test_negative_number_raises(self):
        with self.assertRaises(ValueError):
            sqrt(-1)


class TestMod(unittest.TestCase):
    def test_exact_remainder(self):
        self.assertEqual(mod(10, 3), 1)

    def test_larger_divisor(self):
        self.assertEqual(mod(2, 5), 2)

    def test_modulo_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            mod(10, 0)


class TestSin(unittest.TestCase):
    def test_sin_of_zero(self):
        self.assertAlmostEqual(sin(0), 0)

    def test_sin_of_pi_over_two(self):
        self.assertAlmostEqual(sin(math.pi / 2), 1)

    def test_sin_of_pi(self):
        self.assertAlmostEqual(sin(math.pi), 0, places=6)


class TestCos(unittest.TestCase):
    def test_cos_of_zero(self):
        self.assertAlmostEqual(cos(0), 1)

    def test_cos_of_pi_over_two(self):
        self.assertAlmostEqual(cos(math.pi / 2), 0, places=6)

    def test_cos_of_pi(self):
        self.assertAlmostEqual(cos(math.pi), -1)


if __name__ == "__main__":
    unittest.main()
