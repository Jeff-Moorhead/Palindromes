"""Find the largest palindrome which is the product of two
three-digit numbers."""
import palindrome_functions as pf

products2 = pf.find_two_digit_products()
products3 = pf.find_three_digit_products()
max_palindrome2 = pf.find_max_palindrome(products2)
max_palindrome3 = pf.find_max_palindrome(products3)
print("The largest palindrome made from the product of two-digit numbers is "
      + str(max_palindrome2) + ".")
print("The largest palindrome made from the product of three-digit numbers is "
      + str(max_palindrome3))
