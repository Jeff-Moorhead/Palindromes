"""Performs unit tests for palindromes.py"""

import unittest
import palindrome_functions as pf

class PalindromesTest(unittest.TestCase):
    """Test palidromes.py"""
    def test_is_palindrome(self):
        # Does a palindrome return True?
        true_pali = pf.is_palindrome(90909)
        self.assertTrue(true_pali)

        # Does a non-palindrome return False?
        false_pali = pf.is_palindrome(95466)
        self.assertFalse(false_pali)

    def test_find_max_palindrome(self):
        """Test find_max_palindrome() for two-digit products."""
        products = pf.find_two_digit_products()
        max_palindrome = pf.find_max_palindrome(products)
        self.assertEqual(max_palindrome, 9009)


unittest.main()
