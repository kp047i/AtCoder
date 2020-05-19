s = input()

days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i, day in enumerate(days):
    if s == day:
        print(7 - i)
