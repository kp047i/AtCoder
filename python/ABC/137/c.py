n = int(input())
s = list(input() for _ in range(n))
se = set() 
for i in range(n):
    s[i] = "".join(sorted(s[i]))
    se.add(s[i])

print(se)
print(n - len(se))
