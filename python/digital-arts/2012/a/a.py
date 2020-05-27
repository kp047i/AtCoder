s = input().split()
n = int(input())
ans = ['' for _ in range(len(s))]

is_matched = False
for i in range(n):
    t = input()
    for j, str in enumerate(s):
        if len(t) == len(str):
            is_matched = True
            for k, c in enumerate(t):
                if c != '*' and c != s[j][k]:
                    is_matched = False
                    break
            if is_matched:
                s[j] = '*' * len(s[j])
print(' '.join(s))
