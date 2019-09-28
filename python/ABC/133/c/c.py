l, r = map(int, input().split())
ans = 10 ** 10

for i in range(l, min(r, l + 2019)):
    for j in range(i + 1, min(r, l + 2019) + 1):
        ans = min(ans, i * j % 2019)
print(ans)
