#!/usr/bin/python3
import sys

def factorial(n):
    """
    Computes the factorial of a given number.

    Function Description:
    Recursively calculates the factorial of a non-negative integer `n`. 
    The factorial of `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the input integer `n`. Returns 1 if `n` is 0 (base case).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the integer from command line arguments
f = factorial(int(sys.argv[1]))

# Print the result to the console
print(f)

