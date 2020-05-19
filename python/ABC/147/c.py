n = int(input())

a = []
x = [[]]
y = [[]]

for i in range(n):
    A = int(input())
    a.append(A)
    x.append([])
    y.append([])
    for j in range(A):
        X, Y = map(int, input().split())
        x[i].append(X)
        y[i].append(Y)

for i in range(n):
    for j in range(a[i]):
        if x[i][j] == x[x[i][j]][i]:
            print(x[i][j])
            print(x[x[i][j]][x[i]])
