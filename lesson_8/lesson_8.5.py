dist = {1: 2, 3: 4}
x = dist.copy()
x[1] = 5
print(x, dist)


import copy
dist = {1: 2, 3: 4}
x = copy.copy(dist)
x[1] = 5
print(x, dist)