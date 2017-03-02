import random
randomlist = ([random.randint(0, 100) for i in range(10)])
randomlist = [1, 2, 3, 4, 5]
bool = True
for i in range(len(randomlist)-1):
    if randomlist[i] > randomlist[i+1]:
        bool = False
print(bool)
print(randomlist)
