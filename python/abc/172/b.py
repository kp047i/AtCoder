s = input()
t = input()

ans = 0
for i, c in enumerate(s):
    if c != t[i]:
        ans += 1

print(ans)
