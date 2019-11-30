MOD = 10**9 + 7
'''
参照: http://sucrose.hatenablog.com/entry/2014/12/23/164335

## 定義と性質
「n個のものからk個だけ取り出す場合の数」は、
二項定理の係数として現れることから、二項係数という呼び名がある
※ (x+y)^nを展開したときのx^(n-k)y^kの係数になっている

         n!
nCk = --------
      k!(n-k)!
## 計算方法
単純に計算するとO(k)回のループで特定の二項係数を計算できる
MODを用いる場合は逐次割る

### 動的計画法を用いる場合
nからkまでの二項係数を求める関係式
nC0 = 1, nCn = 1
1<=n and 1<=k<=n-1であるn,kについて

nCk = (n-1)C(k-1) + (n-1)Ck
が成り立つ
この関係はパスカルの三角形として知られている

'''
def make_comb_dp(n):
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
        dp[i][i] = 1
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp

for line in make_comb_dp(5):
    print(line)
