n = int(input())
a = list(map(int, input().split()))

ans = 1
t = 1e18
if 0 in a:
    print(0)
    exit(0)

for i in range(n):
    ans *= a[i]
    if ans > t:
        print(-1)
        exit(0)

print(ans)
