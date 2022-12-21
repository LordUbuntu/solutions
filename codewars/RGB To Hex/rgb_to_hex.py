# Jacobus Burger (2022)
# RGB to HEX converter problem


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


# The better approach I found from other people
def rgb(r, g, b):
    lim = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(lim(r), lim(g), lim(b))
