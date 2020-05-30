h1, m1, h2, m2, k = map(int, input().split())

sub_h = h2 - h1
ans = sub_h * 60 + m2 - m1 - k
print(ans)