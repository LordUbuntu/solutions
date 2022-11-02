# Jacobus Burger (2022)
# Based on a vague memory of a problem from a few weeks back.
# Problem:
#   Order a group of people by first name, but if they have the same first name then order them by last name
# Solution:
#   We can sort a list first by first names and then by last in that order

def first_last_solution():
    N = int(input())  # number of names
    names = [" ".join([name for name in input().split()])
            for _ in range(N)]
    return sorted(names)
