x, y = map(int, input().split())
mod = 10**9 + 7

def com(n, r, mod):
    r = min(r, n-r)
    number = denom = 1
    for i in range(1, 1+1):
        number = number*(n+1-i)%mod
        denom = denom*i%mod
    return number*pow(denom, mod-2)%mod

if (x+y)%3 != 0:
    print(0)
    exit()

n = ((2*x) -y)//3
m = ((x+y)//3)-n

if n<0 or m<0:
    print(0)
    exit(0)

print(com(n+m), min(n,m), mod)
