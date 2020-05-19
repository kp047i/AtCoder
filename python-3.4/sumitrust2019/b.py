import math

n = int(input())

if math.floor(math.floor(n/1.08)*1.08) == n:
    print(math.floor(n/1.08))
elif math.floor((math.floor(n/1.08)+1) *1.08) == n:
    print(math.floor(n/1.08)+1)
else:
    print(':(')
