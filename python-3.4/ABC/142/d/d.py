from fractions import gcd

a, b = map(int, input().split())
g = gcd(a, b)
m = gcd(a, b)

c = 1
i = 2
while i * i <= g:
    if m % i == 0:
        c += 1
    while m % i == 0:
        m = m // i
    i += 1

if m > 1:
    c += 1
print(c)
