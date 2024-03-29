# Jacobus Burger (2023)
# Title:
#   Array plug Array
# Problem:
#   Find the total of the integers in two arrays
# Solution:
#   There's a few ways to do this in python, the most straightforward is to
#   simply concatenate the two arrays and then use the sum builtin fuction to
#   find their total value.
# See:
#   https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/python


def array_plus_array(arr1, arr2: list[int]) -> int:
    return sum(arr1 + arr2)
