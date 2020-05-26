n, m = map(int, input().split())
s = []
c = []
ans = [0 for _ in range(n)]
has_num = [False for _ in range(n)]

for i in range(m):
    S, C = map(int, input().split())
    s.append(S)
    c.append(C)

    if has_num[S - 1] == True and ans[S-1] != C:
        print(-1)
        exit(0)
    has_num[S-1] = True

    ans[S - 1] = C

if ans[0] == 0 and has_num[0] == True and n != 1:
    print(-1)
    exit(0)

if ans[0] == 0 and n != 1:
    ans[0] = 1

maped_ans = map(str, ans)
print(''.join(maped_ans))
