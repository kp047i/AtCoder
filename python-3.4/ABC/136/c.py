n = int(input())
h = list(map(int, input().split()))

c = 0
for i in h:
    if c > i:
        print('No')
        exit()
    elif c < i:
        c = i-1
print('Yes')
