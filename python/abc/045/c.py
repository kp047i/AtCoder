s = input()
n = len(s)
ans = 0

for i in range(2 ** (n - 1)):
    tmp = s[0]
    for j in range(n - 1):
        if ((i >> j) & 1):
            print(i, j)
            tmp += '+'
        tmp += s[j + 1]
    print(tmp)
    ans += eval(tmp)
print(ans)
