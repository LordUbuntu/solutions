# Matrix Transpose

[Source](https://www.codewars.com/kata/52fba2a9adcd10b34300094c/solutions/python)

## Problem Description

Transpose a Matrix ([What is Matrix Transposition](https://en.wikipedia.org/wiki/Transpose). Essentially this is done by rotating a matrix about its diagonal (if that makes any sense).

## Input

A list of lists representing each row in the matrix.

## Output

A list of lists representing each row in the transposed matrix.

## Solution

The straightforward solution is to grab each element in the same column across all rows and make a new row from that, and then repeat that for each row of the new transpose matrix.


The better solution which I soon arrive to was to zip each element of each column in each row together using the `zip` function, converting those tuples to lists, and then putting those in a list. This way felt more Pythonic.
