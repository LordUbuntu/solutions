# RGB to Hex Conversion

[Source](https://www.codewars.com/kata/513e08acc600c94f01000001)

## Problem Description

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

## Input

Three integer values r, g, and b.

## Output

Returns the hex string representation of the RGB values given.

## Solution

My first solution was suboptimal, I would iterate through the arguments given (the rgb colour values) and then append 00 if their value was below 0, ff if their value was above 255, and the python hex representation with some string concatenation magic otherwise.

An alternative solution someone had was to simply use Python's built-in string formatting to print the value (after limiting it) as its hex representation directly.
