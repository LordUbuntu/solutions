# Jacobus Burger (2022)
# Background:
#   While I was training with my team (Jimmy Kha, Yaacov Kotchakov) for
#   the 2022 ICPC in February I came up with an interesting problem
#   for us to solve on the spot.
# Problem:
#   You'll notice that in traffic the turn signals of cars all flash
#   on and off at different intervals, flashing at different times,
#   every-so-often at the same time.
#   Given a series of space-seperated numbers representing the interval
#   of turn signal flashing for each car in a line, determine the number
#   of seconds you would need to wait for all of them to flash at the same
#   time.
# Example:
#   3 4 5  =>  60
# Solution:
#   The solution found was to calculate the least common multiple
#   between all of the input numbers, as that would be the smallest
#   (the first) number that all the inputs would have in common.
from functools import reduce

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def solution(cars):
    return reduce(lcm, cars)


if __name__ == '__main__':
    # T is number of tests      where 0 <= T <= 100
    # each test may have 0 <= N <= 100,000 cars
    # each car may have 1 <= c <= 1,000,000,000
    T = int(input())
    for _ in range(T):
        cars = [int(n) for n in input().split()]
        print(solution(cars))
