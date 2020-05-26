import math

txa, tya, txb, tyb, t, v = map(int, input().split())
n = int(input())
x = []
y = []

for i in range(n):
    X, Y = map(int, input().split())
    x.append(X)
    y.append(Y)
    distance_from = math.sqrt((txa - X) ** 2 + (tya - Y) ** 2)
    distance_to = math.sqrt((txb - X) ** 2 + (tyb - Y) ** 2)
    if distance_from + distance_to <= t * v:
        print('YES')
        exit(0)

print('NO')
