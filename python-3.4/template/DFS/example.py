# 深さ優先探索とは
# 取り合えずスタートから末端まで進めるまで進んで、進めるところがなくなったら1つ前に戻ってまだ進んでいない分岐を進む
# 進んでいない分岐がなかったらもう一つ戻ってまだ進んでいない分岐を進む
# 繰り返し
# 現在の深さとみてる要素を対応付ける

from collections import deque

h, w = map(int, input().split())
maze = list(list(input()) for _ in range(h))

for j in range(h):
    for i in range(w):
        if maze[j][i] == 's':
            sy, sx = j, i
        if maze[j][i] == 'g':
            gy, gx = j, i

dq = deque()
dq.append([sy, sx])

while len(dq) > 0:
    y, x = dq.pop()
    if y == gy and x == gx:
        print("Yes")
        exit()
    for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        ny, nx = [y + dy, x + dx]
        if 0 <= ny < h and 0 <= nx < w and maze[ny][nx] != '#':
            dq.append([ny, nx])
            maze[ny][nx] = "#"
print("No")

