from collections import defaultdict
import heapq

n, m = map(int, input().split())
d = defaultdict(list)

for _ in range(n):
    a, b = map(int, input().split())
    d[a].append(-b)

hq = []
reword = 0

for i in range(1, m + 1):
    if i in d:
        for item in d[i]:
            heapq.heappush(hq, item)
    if hq:
        reword += heapq.heappop(hq)

print(-1 * reword)
