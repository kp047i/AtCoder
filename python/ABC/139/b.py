a, b = map(int, input().split())

c = 0
while (a * c - (c - 1)) < b:
    c += 1

print(c)
