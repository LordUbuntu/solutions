# Cats and Shelves

## Problem Description

An infinite number of shelves are arranged one above the other in a staggered fashion. The cat can jump up to 3 shelves or 1 shelf but cannot jump to the shelf directly above it (a jump of 2). Illustrated:

```
                 ┌────────┐
                 │-6------│
                 └────────┘
┌────────┐       
│------5-│        
└────────┘  ┌─────► OK!
            │    ┌────────┐
            │    │-4------│
            │    └────────┘
┌────────┐  │
│------3-│  │     
BANG!────┘  ├─────► OK! 
  ▲  |\_/|  │    ┌────────┐
  │ ("^-^)  │    │-2------│
  │ )   (   │    └────────┘
┌─┴─┴───┴┬──┘
│------1-│
└────────┘
```

Your goal is to determine the minimum number of jumps to get from a given start shelf to a given finish shelf.

## Input

Two positive integers `start` and `finish`, `finish` will be no smaller than `start`.

## Output

Return the minimum number of jumps/steps to get from the start to the finish.

## Solution

I first approached the problem by exploring mathematical relations like the evenness and oddness of the `start` number, the `finish` number, their sum, their difference. When I examined the minimum jumps of various different `start` and `finish` chains, I realized that the answer was always to take as many jumps of 3 from the `start` to the `finish` without overshooting the `finish`, and then taking jumps of 1 to reach the `finish` if we weren't there yet.

That made me realize that the answer was to take the difference of `start` and `finish` (to determine only the steps in that gap), divide that by 3, and then add the quotient and remainder of that division.

As equations that would look like:

$$\mathit{quotient} = \frac{\mathit{finish} - \mathit{start}}{3}$$
$$\mathit{remainder} = \mathit{finish} - \mathit{start} \mod 3$$
