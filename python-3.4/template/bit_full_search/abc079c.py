s = input()
for i in range(2 ** len(s) - 1):
    tmp = s[0]
    for j in range(len(s) - 1):
        if ((i >> j) & 1):
            tmp += '+'
        else:
            tmp += '-'
        tmp += s[j + 1]
    if(eval(tmp) == 7):
        print(tmp + "=7")
        break
