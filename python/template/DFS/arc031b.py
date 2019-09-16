import copy
from collections import deque


maze = list(list(input()) for _ in range(10))
copied_maze = copy.deepcopy(maze)

def dfs(x, y):
    dq = deque()
    dq.append([x, y])
    copied_maze[x][y] = 'o'
    while len(dq) > 0:
        x, y = dq.pop()
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx, ny = [x + dx, y + dy]
            if 0 <= nx < 10 and 0 <= ny < 10 and copied_maze[nx][ny] != 'x':
                dq.append([nx, ny])
                copied_maze[nx][ny] = "x"

def check(maze):
    for i in range(10):
        for j in range(10):
            if maze[i][j] == 'o':
                return False
    return True

for i in range(10):
    for j in range(10):
        if maze[i][j] == 'x':
            copied_maze = copy.deepcopy(maze)
            dfs(i, j)
            if check(copied_maze):
                print("YES")
                exit()

print("NO")

