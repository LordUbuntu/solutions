# Jacobus Burger (2022-12-09)
# I'm not sure if this problem exists elsewhere (it does, "towers of hanoi").
# Basically, try to determine the number of steps of a tower of n disks


# the minimal number of moves for hanoi is 2^n - 1
# I solved that by realizing that 2 disks take 3 steps and
#   3 disks take 7, which follow that pattern.
class Solution:
    def hanoi(disks):
        return 2**disks - 1
