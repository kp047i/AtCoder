s = input()

f = True
for i in range(len(s)):
    if i % 2 == 1:
        if s[i] == 'R':
            f = False
    else:
        if s[i] == "L":
            f = False
if f == True:
    print("Yes")
else:
    print("No")
