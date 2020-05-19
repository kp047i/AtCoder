a, b, x = map(int, input().split())

digit = len(str(b))
_max = 0
ans = 0
for i in reversed(range(x//a+1)):
    if a*i < x:
        if a*i + digit*b < x:
            if ans < a*i + digit*b:
                _max = a*i + digit*b
                ans = i

print(ans)
