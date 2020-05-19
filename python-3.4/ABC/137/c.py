n = int(input())
s = list(input() for _ in range(n))
ans = 0
d = {}
for i in range(n):
    s[i] = "".join(sorted(s[i]))
    if s[i] not in d.keys():
        d[s[i]] = 0
    else:
        d[s[i]] += 1
        ans += d[s[i]]

print(ans)
