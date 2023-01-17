# Jacobus Burger (2023)
# Matrix Transpose Problem
# See: https://www.codewars.com/kata/52fba2a9adcd10b34300094c/solutions/


# get each column element for each row, make a row
#   from that, and return those rows together.
def nieve_solution(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


# zip each element across each row
#   [1, 2], [3, 4]  =>  (1, 3), (2, 4)
def zip_solution(matrix):
    return list(map(list, zip(*matrix)))
