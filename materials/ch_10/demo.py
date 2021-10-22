import math

pi = math.pi
print(pi)

XLIST = [0, 30, 60, 90]

for x in XLIST:
    y = math.sin(x)
    print(f'y = sin({x}) = {y}')

for x in XLIST:
    y = math.sqrt(x)
    print(f'y = sqrt({x}) = {y}')

lcm = math.lcm(30, 60, 90)
print('ครน ของ 30, 60, 90', 'คือ', lcm)

gcd = math.gcd(30, 60, 90)
print('หรม ของ 30, 60, 90', 'คือ', gcd)