import random

li = []

dec = 0
for j in range(4):
    x = random.randint(0, 1)
    li.append(x)
    s = [str(x) for x in li]
    res = ("".join(s))
    dec = int(res, 2)
print(dec)
