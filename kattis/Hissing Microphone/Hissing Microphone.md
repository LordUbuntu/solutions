# Hissing Microphone

## Problem Description

Some microphones have a "hissing s". That is, sometimes the sound of the letter s is over-pronounced, producing a nice hissing sound. Words that have two consecutive s ("ss") produce this sound. Find out whether a given word will or won't produce the "hissing s".

## Input

A word that will be spoken into the microphone (a string).

## Output

Print "hiss" if the microphone will hiss, and "no hiss" if it won't.

## Solution

Thanks to the `in` keyword in Python, we can simply check if an "ss" is in the input, and print "hiss" or "no hiss" depending on if it is (or isn't).
