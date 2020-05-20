n, a, b = map(int, input().split())

if a > b:
    print(0)
    exit(0)
if n == 1:
    if a == b:
        print(1)
        exit(0)
    else:
        print(0)
        exit(0)
print((n-2) * (b-a) + 1)