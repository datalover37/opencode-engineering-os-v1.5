"""Unit tests for the calculator module.

Covers:
    - Correct arithmetic for int and float operands.
    - TypeError for bool operands (both a and b positions).
    - TypeError for unsupported operand types (string, list, None).
    - Both add() and subtract().
"""

import unittest

from src.calculator import add, subtract


class TestAdd(unittest.TestCase):
    """Tests for the add() function."""

    def test_add_two_ints(self):
        self.assertEqual(add(3, 5), 8)

    def test_add_int_and_float(self):
        self.assertAlmostEqual(add(2, 3.5), 5.5)

    def test_add_two_floats(self):
        self.assertAlmostEqual(add(1.2, 3.4), 4.6)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, 3), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 7), 7)

    def test_add_bool_a_raises_typeerror(self):
        with self.assertRaises(TypeError):
            add(True, 5)

    def test_add_bool_b_raises_typeerror(self):
        with self.assertRaises(TypeError):
            add(5, False)

    def test_add_bool_both_raises_typeerror(self):
        with self.assertRaises(TypeError):
            add(True, False)

    def test_add_string_raises_typeerror(self):
        with self.assertRaises(TypeError):
            add("hello", 3)

    def test_add_list_raises_typeerror(self):
        with self.assertRaises(TypeError):
            add([1, 2], 3)

    def test_add_none_raises_typeerror(self):
        with self.assertRaises(TypeError):
            add(None, 5)


class TestSubtract(unittest.TestCase):
    """Tests for the subtract() function."""

    def test_subtract_two_ints(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 7), -4)

    def test_subtract_float_result(self):
        self.assertAlmostEqual(subtract(5.5, 2.0), 3.5)

    def test_subtract_int_and_float(self):
        self.assertAlmostEqual(subtract(10, 3.2), 6.8)

    def test_subtract_zero(self):
        self.assertEqual(subtract(8, 0), 8)

    def test_subtract_bool_a_raises_typeerror(self):
        with self.assertRaises(TypeError):
            subtract(True, 5)

    def test_subtract_bool_b_raises_typeerror(self):
        with self.assertRaises(TypeError):
            subtract(5, False)

    def test_subtract_bool_both_raises_typeerror(self):
        with self.assertRaises(TypeError):
            subtract(True, False)

    def test_subtract_string_raises_typeerror(self):
        with self.assertRaises(TypeError):
            subtract("world", 3)

    def test_subtract_list_raises_typeerror(self):
        with self.assertRaises(TypeError):
            subtract([1], 2)

    def test_subtract_none_raises_typeerror(self):
        with self.assertRaises(TypeError):
            subtract(None, 5)


if __name__ == "__main__":
    unittest.main()
