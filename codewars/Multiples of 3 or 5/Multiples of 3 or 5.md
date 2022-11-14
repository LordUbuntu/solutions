# Multiples of 3 or 5

## Problem Description

Find the sum of all integers up to a given number `number` which are multiples of either (inclusive) 3 or 5.

For example, if `number` is 6, then the answer is 8, since 3 + 5 = 8.

## Input

An integer `number` representing the exclusive stop of the range.

## Output

The sum of all multiples of 3 or 5 up to but excluding `number`.

## Solution

We loop over all numbers from 0 to `number` and keep a running total if that number is divisible by either 3 or 5. Then we return the total.

## Extra

I found an interesting and novel solution which I explained to someone else.

```python
def solution(number):
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result
```

As I understand it, it essentially uses number theory to determine the number of 3's, 5's, and 15's in the range in linear time, and then uses set theory to find the sum of all the 3's and 5's, excluding all 15's in that range.

Let A be all multiples of 3, then `a3 = (number - 1) / 3` is calculating the cardinality of A. The interesting parts comes at the result line. It takes the form of n(n + 1)/2 to find the triangular sum of the given multiple (be it 3, 5, or 15). Then, multiplies that answer by the given multiple to obtain the sum of all that multiple within the range. Finally we take the difference of multiples 3 and 5 have in common from the multiples they don't have in common, and the result is incredibly the sum of all multiples of 3 or 5 up to the given number.

This inspired me to write my own set theory notation example which makes this more explicit:

```python
def solution(number):
  A = {n for n in range(0, number, 3)}  # all multiples of 3
  B = {n for n in range(0, number, 5)}  # all multiples of 5
  C = {n for n in range(0, number, 15)} # all multiples of both (of 15)
  return sum(A.union(B).difference(C))
```

However, this doesn't seem to work on all cases. I'm not sure what the discrepancy is there.
