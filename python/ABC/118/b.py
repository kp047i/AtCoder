n, m = map(int, input().split())
s = set(range(1, m + 1))
for i in range(n):
    k, *a = map(int, input().split())
    a = set(a)
    s &= a
print(len(s))
