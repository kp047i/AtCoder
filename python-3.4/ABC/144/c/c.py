n = int(input())

cd = []
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        cd.append(i)
        if i != n // i:
            cd.append(n//i)
min = float('inf')
if len(cd) % 2 == 0:
    for i in range(0, len(cd) - 1,  2):
        if cd[i] + cd[i+1] < min:
            min = cd[i] + cd[i+1]
    print(min - 2)
else:
    print(cd[len(cd) - 1] * 2 - 2)

