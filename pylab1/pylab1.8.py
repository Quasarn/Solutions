import random
n = random.randint(0,10)
randomlist = ([random.randint(0, 100) for i in range(n)])
i = 0
while 2**i <= n:
    i += 1
for j in range(2**i-len(randomlist)):
    randomlist.append(0)
print(n, ' ', i, ' ', len(randomlist))
print(randomlist)
