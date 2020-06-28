n, q = map(int, input().split())
a = list(map(int, input().split()))
x = list(map(int, input().split()))

# q回分のクエリを実行
for i in range(q):
    ans = 0

    # 区間の左端で場合分け
    right = 0
    _sum = 0
    for left in range(n):
        # sumにa[right]を加えても大丈夫ならrightを動かす
        while right < n and (_sum + a[right]) <= x[i]:
            _sum += a[right]
            right += 1
        
        # breakした状態でrightは条件を満たす最大
        ans += right - left
        
        # right == leftだったらその区間の最大の個数まで到達
        if right == left:
            right += 1
        # それ以外はleftだけがインクリメントされるようにsumからa[left]を引いていく
        else:
            _sum -= a[left]
        # 条件を満たせなくなるまでrightを増やしたので今度はleftをrightからスタート

    print(ans)

