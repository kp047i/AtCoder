n = int(input())
s = input()

if n%2 == 1:
    print('No')
    exit()
else:
    for i in range(n//2):
        if s[i] != s[n//2+i]:
            print('No')
            exit()

print('Yes')
