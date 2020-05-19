import math

n, m = map(int, input().split())

sh = n % 12

sh_angle = (sh + m/60)*2*math.pi/ 12
big_angle = m * 2 * math.pi / 60
ang = abs(sh_angle - big_angle)
print(min(math.degrees(ang), 360 - math.degrees(ang)))

