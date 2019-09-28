import math


n, d = map(int, input().split())
x = [list(map(int, list(input().split()))) for _ in range(n)]
c = 0

for i in range(n):
    for j in range(i + 1, n):
        sum = 0
        for k in range(d):
            sum += pow(x[i][k] - x[j][k], 2)
        if math.sqrt(sum).is_integer():
            c += 1

print(c)
