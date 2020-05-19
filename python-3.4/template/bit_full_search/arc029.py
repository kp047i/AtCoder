n = int(input())
t = list(int(input()) for _ in range(n))

ans = 200
for i in range(2 ** n):
    a = []
    b = []
    for j in range(n):
        if ((i >> j) & 1):
            a.append(t[j])
        else:
            b.append(t[j])
    if sum(a) >= sum(b):
        tmp = sum(a)
    else:
        tmp = sum(b)
    if tmp <= ans:
        ans = tmp
print(ans)
