from collections import deque


n, q = map(int, input().split())
a = []
b = []
p = []
x = []
score = [0 for i in range(n)]
tree = {i:[] for i in range(1, n + 1)}

def dfs(p, x):
    for i in tree[p]:
        if i > p:
            score[i - 1] += x
        score[p - 1] += x
for i in range(n - 1):
    i_a, i_b = map(int, input().split())
    a.append(i_a)
    b.append(i_b)
    tree[i_a].append(i_b)
    tree[i_b].append(i_a)

for i in range(q):
    i_p, i_x = map(int, input().split())
    dfs(i_p, i_x)
    print(i, end = " : ")
    print(score)

print(score)

