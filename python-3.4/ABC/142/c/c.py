n = int(input())
a = list(map(int, input().split()))

dic = {}
for i in range(n):
    dic[i + 1] = a[i]

sorted_dic = sorted(dic.items(), key=lambda x:x[1])

for i in range(n):
    print(sorted_dic[i][0], end=" ")
