import calendar
import time

for x in range(2000, 2031):
    y = calendar.isleap(x)
    print(f'YEAR {x} -> LEAP_YEAR = {y}')

for d in calendar.day_name:
    print(d)

print('NOW IS', time.ctime())

XLIST = [10, 20, 30, 40]
for x in XLIST:
    print(f'x = {x} ...')
    time.sleep(5)