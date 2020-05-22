n = input()

sum_odd = 0
sum_even = 0
for i in range(len(n)):
    if i % 2:
        sum_odd += int(n[i])
    else:
        sum_even += int(n[i])

if len(n) % 2:
    print(sum_odd, sum_even)
else:
    print(sum_even, sum_odd)
