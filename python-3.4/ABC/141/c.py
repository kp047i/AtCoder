n, k, q = map(int, input().split())

a = []
for i in range(q):
    a.append(int(input()))

point = [0 for _ in range(n)]

for i in range(q):
    point[a[i] - 1] += 1

for i in range(n):
    if k - q + point[i] > 0:
        print("Yes")
    else:
        print("No")
