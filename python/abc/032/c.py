n, k = map(int, input().split())
s = []

for _ in range(n):
    S = int(input())
    if S == 0:
        print(n)
        exit(0)
    s.append(S)

# 4 3 1 1 2 10 2

ans = 0
right = 0
product = 1
for left in range(n):
    while right < n and product * s[right] <= k:
        product *= s[right]
        right += 1
    ans = max(ans, right - left)
    if right == left:
        right += 1
    else:
        product /= s[left]
print(ans)


