n = int(input())

c = False
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == n:
            c = True
if c == True:
    print('Yes')
else:
    print('No')
