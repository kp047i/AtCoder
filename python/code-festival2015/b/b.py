n, m = map(int, input().split())
a = list(map(int, input().split()))

numeric = list(0 for _ in range(m + 1))

for A in a:
    numeric[A] += 1

max_num = 0
for i, n in enumerate(numeric):
    if n > max_num:
        max_num = n
        max_index = i

if max_num > len(a)/2:
    print(max_index)
else:
    print('?')

    # max_num = 0
    # for i in range(m + 1):
    #     if max_num < a.count(i):
    #         max_num = a.count(i)
    #         max_index = i
    # if max_num > len(a)/2:
    #     print(max_index)
    # else:
    #     print('?')
