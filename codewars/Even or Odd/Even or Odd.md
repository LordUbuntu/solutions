# Even or Odd

## Problem Description

Create a function that returns "Even" for even numbers, and "Odd" for odd numbers.

## Input

An integer `number`

## Output

The string `"Odd"` or `"Even"` returned (not printed) by the function.

## Solution

Remember that all even numbers can be expressed as some multiple of 2. Then that means any number divisible by 2 is even, and conversely if it has a remainder (not divisible by 2) then it is odd. Thus, we just return `"Even"` when the number is divisible by 2, and `"Odd"` otherwise.
