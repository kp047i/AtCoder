s = input()

l = len(s)
c = 0
for i in range(l):
    if s[i] != s[l-i-1]:
        c += 1
print(c//2)
