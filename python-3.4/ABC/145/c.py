import math
import itertools

n = int(input())

x = []
y = []
l = []

for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    l.append(i)    

sum_distance = 0
c = 0

for p in itertools.permutations(l):
    for i in range(n-1):
        sum_distance += ((x[p[i]]-x[p[i+1]])**2 + (y[p[i]]-y[p[i+1]])**2)**0.5

print(sum_distance/math.factorial(n))
