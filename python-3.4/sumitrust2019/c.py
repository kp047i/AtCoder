import itertools
import math
x = int(input())
 
remain = x % 100
quotient = math.floor(x/100)
 
items = [100, 101, 102, 103, 104, 105]
n = 6
 
for moneys in itertools.combinations_with_replacement(items, quotient):
    if sum(moneys) == x:
        print(1)
        exit()
print(0)
