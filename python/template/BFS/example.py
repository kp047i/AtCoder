# 幅優先探索
#幅優先探索とは、木構造やグラフの探索を行うためのアルゴリズムです。始点となるノードから隣接するノードを探索し、そこからさらに隣接するノードにたいして探索を繰り返して目的のノードを見つます。幅優先探索は全ノードを網羅的に探索していくため、しらみつぶしに調べていく方法とも言えます。

#始点から近い順に探索をしていくため、探索するのノードは キュー(FIFO) を使って管理することになります。深さ優先探索が スタック(LIFO) を使って管理する点に対して対称的なアルゴリズムにです。

# アルゴリズム
# 1.始点のノードを探索待ちキューに追加する。
# 2. 探索待ちキューにノードがあれば取り出す。なければ全ノード探索完了。
# 3.取り出したノードが目的ノードであれば探索完了。
# 4. 取り出したノードに隣接するノードの内、未探索のノードを探索待ちキューに追加する。
# 5. 2. の処理にもどる。

from collections import deque
INF = float("inf")

r, c =  map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
sx, sy = sx - 1, sy - 1
gx, gy = gx - 1, gy - 1
maze = list(list(input()) for _ in range(r))
depth = [[INF for i in range(c)] for j in range(r)]

dq = deque()
dq.append([sx, sy])
depth[sx][sy] = 0
while len(dq) > 0:
    x, y = dq.popleft()
    if x == gx and y == gy:
        print(depth[gx][gy])
        break
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx, ny = [x + dx, y + dy]
        if 0 <= nx < r and 0 <= ny < c and maze[nx][ny] != '#' and depth[nx][ny] == INF:
            dq.append([nx, ny])
            depth[nx][ny] = depth[x][y] + 1
