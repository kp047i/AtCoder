n = int(input())

a = [int(input()) for _ in range(n)]
sorted_a = sorted(a, reverse=True)

for i in range(n):
    if a[i] != sorted_a[0]:
        print(sorted_a[0])
    else:
        print(sorted_a[1])
