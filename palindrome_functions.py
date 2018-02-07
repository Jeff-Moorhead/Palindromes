"""Functions for palindrome.py"""


def is_palindrome(num):
    """Test if a number is a palindrome."""
    # Convert num to a string to compare indices.
    num = str(num)
    half = len(num) // 2
    forward = ''
    backward = ''
    for i in range(half):
        forward += num[i]
        backward += num[-(i + 1)]
    if forward == backward:
        return True
    else:
        return False


def find_two_digit_products():
    """Find all the products of every two digit number."""
    products = []
    for i in range(10, 100):
        for j in range(10, 100):
            products.append(i * j)
    return products


def find_three_digit_products():
    """Find all the products of every three digit number."""
    products = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            products.append(i * j)
    return products


def find_max_palindrome(li):
    """Find the max palindrome in a list of ints"""
    palindromes = []
    for num in li:
        if is_palindrome(num):
            palindromes.append(num)
    return max(palindromes)
