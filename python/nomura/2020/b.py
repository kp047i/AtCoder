t = input()
ans = []

for i in range(len(t)):
    ans.append(t[i])

for i in range(len(t)):
    if ans[i] == '?':
        ans[i] = 'D'
print(''.join(ans))
