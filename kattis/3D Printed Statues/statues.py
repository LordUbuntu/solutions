# 3d printed statues
# we divide by 2 and sub 1 until we arrive at a value <= 0, step # is ans
# credit to Yaacov for figuring out the final implementation here.

# for n statues, we take d days
n = int(input())
d = 0
while n > 0:
    if n > 1:
        n /= 2
    else:
        n -= 1
    d += 1
print(d)
