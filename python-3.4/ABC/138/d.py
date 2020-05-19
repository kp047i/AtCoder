from collections import deque


n, q = map(int, input().split())
tree = [[] for _ in range(n + 1)]
score = [0 for _ in range(n + 1)]

dq = deque()
dq.append((1, 0))

for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(q):
    p, x = map(int, input().split())
    score[p] += x

while(dq):
    k = dq.popleft()
    score[k[0]] += score[k[1]]
    for i in tree[k[0]]:
        if not i == k[1]:
            dq.append((i, k[0]))

print(*score[1:])
