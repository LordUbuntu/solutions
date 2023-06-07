# Jacobus Burger (2023)
# Title:
#   Matrix Transpose
# Problem:
#   Transpose A Matrix
# Solution:
#   The straightforward solution is to grab each element in the same column
#   across all rows and make a new row from that, and then repeat that for each
#   row of the new transpose matrix.
#   The better solution which I soon arrived to was to zip each element of each
#   column in each row together using the `zip` function, converting those
#   tuples to lists, and then putting those in a list. This way felt more
#   Pythonic.
# See:
#   https://www.codewars.com/kata/52fba2a9adcd10b34300094c/solutions/
#   https://en.wikipedia.org/wiki/Transpose


# get each column element for each row, make a row
#   from that, and return those rows together.
def nieve_solution(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


# zip each element across each row
#   [1, 2], [3, 4]  =>  (1, 3), (2, 4)
def zip_solution(matrix):
    return list(map(list, zip(*matrix)))
