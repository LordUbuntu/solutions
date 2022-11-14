# Jacobus Burger (2022)
# if any number is a multiple or either 3 or 5 then it is divisible by either 3 or 5
# thus, we simply add the number to a running total if it is divisible by either 3 or 5 (inclusive)
def solution(number):
    total = 0
    if number < 0:
        return 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


# one interesting mathematical solution by some other people caught my
# attention. It calculates the total of the multiples of 3, adds them to 
# the total of the multiples of 5, and then subtracts from that the total
# of the multiples of 15.
def solution(number):
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result
