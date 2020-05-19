n = int(input())
v = list(map(int, input().split()))

v.sort()
tmp = []
tmp.append(v[0])
for i in range(n):
    tmp.append((tmp[i] + v[i]) / 2)

print(tmp.pop())
