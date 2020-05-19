n = int(input())
h = list(map(int, input().split()))

l = list(0 for _ in range(n))

for i in range(1, n):
    if h[i - 1] >= h[i]:
        l[i] = l[i - 1] + 1

print(max(l))

