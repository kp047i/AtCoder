import math

a, b, x = map(int, input().split())

if a ** 2 * b / 2 <= x:
    print(math.degrees(math.atan(2 * (a ** 2 * b - x) / (a ** 3))))
else:
    print(math.degrees(math.pi / 2 - math.atan(2 * x / (a * b ** 2))))
