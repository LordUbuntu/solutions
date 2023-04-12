# Jacobus Burger (2023)
# See:
#   https://open.kattis.com/problems/simonsays
N = int(input())
for _ in range(N):
    command = input().split()
    if command[:2] == ["Simon", "says"]:
        print(' '.join(command[2:]))
