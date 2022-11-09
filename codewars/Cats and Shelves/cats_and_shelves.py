# Jacobus Burger (2022)
# Problem:
#
# Solution:
#   The minimum number of jumps is the number of jumps of 3 we can do
#   without overshooting plus the number of jumps of 1 remaining, from
#   the start to the finish.
#   Put mathematically, the sum of the quotient and remainder of
#   dividing the difference of the finish and the start by 3.
#   jumps = (((finish - start) // 3) + ((finish - start) % 3))
def solution(start, finish):
    return ( (finish - start) // 3 ) + ( (finish - start) % 3 )
    # or `return sum(divmod(finish - start, 3))`
