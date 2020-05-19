import itertools

MOD = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))
l = [i for i in range(n)]
com_l = list(itertools.combinations(l, 2))

ans = 0
for i in range(len(com_l)):
    ans += a[com_l[i][0]] ^ a[com_l[i][1]]
    ans = ans % MOD
print(ans)
