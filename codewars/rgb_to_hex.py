# Jacobus Burger (2022)
# Title:
#   RGB to Hex
# Problem:
#   The rgb function is incomplete. Complete it so that passing in RGB decimal
#   values will result in a hexadecimal representation being returned. Valid
#   decimal values for RGB are 0 - 255. Any values that fall out of that range
#   must be rounded to the closest valid value.
# Solution:
#   My first solution was suboptimal, I would iterate through the arguments
#   given (the rgb colour values) and then append 00 if their value was below 0,
#   ff if their value was above 255, and the python hex representation with some
#   string concatenation magic otherwise.
#
#   An alternative solution someone had was to simply use Python's built-in
#   string formatting to print the value (after limiting it) as its hex
#   representation directly.
# See:
#   https://www.codewars.com/kata/513e08acc600c94f01000001


# My original solution
def rgb(r, g, b):
    string = ""
    for colour in [r, g, b]:
        if colour < 0:
            string += "00"
        elif colour > 255:
            string += "ff"
        else:
            repr = hex(colour)[2:]
            string += repr if len(repr) > 1 else '0' + repr
    return string.upper()


# The better approach I learned
def rgb(r, g, b):
    lim = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(lim(r), lim(g), lim(b))
