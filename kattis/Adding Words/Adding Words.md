# Adding Words

## Problem Description

We want to calculate definitions and equations involving addition and subtraction using words instead of variables. We want to output the answer to each given calculation.

## Input

Up to 2000 commands, one per line, ending at an end of file. Each command can be a defition, calculation, or a clear. All tokens in a command are space-separated. Each definition has the form `def x y` where `x` is the variable name and `y` is an integer from -1000 to +1000. Defining a variable again will overwrite its value with the newest definition. A calculation is of the form `calc foo + bar =`, always starting and ending with a `calc` and `=`. The bit in between is an equation of variable names seperated by a `+` or `-`. A clear command forgets all definitions.

## Output

For any calculations, print `unknown` unless the result maps to a defined variable, then print the variable name instead.

## Example

### Input

```
def foo 3
calc foo + bar =
def bar 7
def programming 10
calc foo + bar =
def is 4
def fun 8
calc programming - is + fun =
def fun 1
calc programming - is + fun =
clear
```

### Output

```
foo + bar = unknown
foo + bar = programming
programming - is + fun = unknown
programming - is + fun = bar
```

## Solution

We just parse input, performing the required operation depending on the variable used. We need to substitute and then evaluate when calc appears.
