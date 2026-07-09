import math
import random

s = [10, 8, 6, 13, 21]
i = 0
v = s[i]
T = 50
a = 0.8
n = 0.6

while T > 0.01:
    j = i + random.uniform(-n, n)
    j = int(round(j))
    j = max(0, min(len(s) - 1, j))
    
    nv = s[j]
    d = nv - v
    
    if d < 0:
        i = j
        v = nv
    else:
        p = math.exp(-d / T)
        if random.random() < p:
            i = j
            v = nv
    
    T = T * a

print(v)
print(i)