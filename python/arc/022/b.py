n = int(input())
a = list(map(int, input().split()))

ans = 0
right = 0
_sum = 0

s = set()
for left in range(n):
    while right < n and a[right] not in s:
        s.add(a[right])
        right += 1
    ans = max(ans, right - left)
    if left == right:
        right += 1
    else:
        s.discard(a[left])
print(ans)
