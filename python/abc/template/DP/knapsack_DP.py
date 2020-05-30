# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=jp

n, W = map(int, input().split())
weight = []
value = []
for _ in range(n):
    v, w = map(int, input().split())
    value.append(v)
    weight.append(w)

dp = [[0]*(W+1) for _ in range(n+1)]

for i in range(n - 1, -1, -1):
    for j in range(W + 1):
        if j < weight[i]:
            dp[i][j] = dp[i + 1][j]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - weight[i]] + value[i])

print(dp)
print(dp[0][W])
