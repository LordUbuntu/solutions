# Take Two Stones

## Problem Description

Alice and Bob are playing a game of stones. There are N stones placed on the ground forming a sequence. The stones are labelled from 1 to N.

Alice and Bob take turns taking exactly two consecutive stones each until there are no consecutive pairs of stones left. If the number of stones left is odd, Alice wins. Otherwise, Bob wins.

**Assuming both Alice and Bob play optimally and Alice plays first, who will win?**

## Input

The input contains an integer N (1 <= N <= 10000000), the number of stones.

## Output

Output the winner, `Alice` or `Bob` on the line.

## Solution

Observe that $$e = 2k$$ and $$o = 2k + 1$$. This means then that given a starting number n, if $$n \mod 2 = 0$$, then Bob would win, but if $$n \mod 2 \neq 0$$ then Alice would win.

In other words, if the number we start with is even, then the number we end with is even, otherwise odd.
