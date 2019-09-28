n, d = map(int, input().split())

num = d * 2 + 1
if n % num == 0:
    print(n // num)
else:
    print(n // num + 1)
