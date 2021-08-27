'''
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
...
5 * 12 = 60
'''

n = int(input('Enter an integer: '))
k = 1
while k <= 24:
    print(n, ' * ', k, '=', n*k)
    k = k + 1