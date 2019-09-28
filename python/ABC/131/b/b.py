n, l = map(int, input().split())

a = [l + i for i in range(n)]
print(sum(a) - min(a, key=abs))
