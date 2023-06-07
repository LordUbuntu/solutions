# Jacobus Burger (2023)
# Title:
#   Even or Odd
# Problem:
#   Create a function that returns "Even" for even numbers,
#   and "Odd" for odd numbers.
# Solution:
#   Remember that all even numbers can be expressed as some multiple of 2. Then
#   that means any number divisible by 2 is even, and conversely if it has a
#   remainder (not divisible by 2) then it is odd. Thus, we just return `"Even"`
#   when the number is divisible by 2, and `"Odd"` otherwise.
# See:
#   https://www.codewars.com/kata/53da3dbb4a5168369a0000fe

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"
