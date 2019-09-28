from fractions import gcd


a, b, c, d = map(int, input().split())
lcm = int(c * d / gcd(c, d))
A = a - 1
l_cd = A - A // c - A // d + A // lcm
r_cd = b - b // c - b // d + b // lcm
print(r_cd - l_cd)
