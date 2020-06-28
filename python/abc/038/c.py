n = int(input())
a = list(map(int, input().split()))

right = 0
ans = 0
_sum = 0
for left in range(n):
    while right < n and (right <= left or a[right - 1] < a[right]):
        right +=1
    ans += right - left
    if right == left:
        right += 1

print(ans)