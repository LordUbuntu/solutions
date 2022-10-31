# 3D Printed Statues

## Problem Description

You have a single 3D printer, and would like to use it to produce n statues. However, printing a statue takes a day, so it may be more efficient to print a new printer instead. That new printer may be used to print statues or even more printers.

**What is the minimum possible number of days needed to print at least n statues?**


## Input

The input contains a single integer n (1 <= n <= 10000), the number of statues you need to print.

## Output

Output a single integer, the minimum number of days needed to print at least n statues.


## Solution

This can be seen of as a problem to go from n to 0 using only division by 2 and subtraction by 1 (kind of like a binary search) in the least number of steps. So to solve this problem we simply need to take the number of statues `n`, and then divide s by 2 while it's greater than 1, then subtract by 1. The resulting count `d` is the minimum number of days needed to print those n statues.
