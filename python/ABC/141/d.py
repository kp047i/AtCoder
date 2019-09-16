import heapq

n, m = map(int, input().split())


# 計算量O(nm)じゃ間に合わない
# 最大値を求める計算量をlogmにする
# 優先度付きキューを使えば、ある優先度に従って優先度の高いものから順に取り出すことができる
# 優先度が1番高い要素を効率良く取り出せるヒープというデータ構造を用いて実装する
# ヒープは2分木で子ノードを2つ持ち親は子よりも必ず大きな値を持つという特性がある

# pythonにはheapqとQueue.PriorityQueueというライブラリがある
# Queue.PriorityQueueはスレッドセーフクラスですが、heapqモジュールはスレッドセーフを保証しません。

# heapqを用いて実装する
# heapqは一番小さい要素を根に持つのでマイナスをかけて実装する

a = [-int(x) for x in input().split()]

# heapq.heapifyでヒープに変換する
heapq.heapify(a)

for i in range(m):
    # heapqから一番小さい値を取り出す
    t = -heapq.heappop(a)
    # tを2で割って切り捨てした値をheapqに格納する
    # 切り捨ての関係でマイナスをかける
    heapq.heappush(a, (t // 2) * (-1))

print(-sum(a))
