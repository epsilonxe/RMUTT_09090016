for k in range(1, 11):
    print('Hello', k)

print('-' * 30)
for member in [2, 3, 5, 7, 11, 13, 17]:
    print(member, 'is prime number')

print('-' * 30)
for member in {2, 3, 5, 7, 11, 13, 17}:
    print(member, 'is prime number')

print('-' * 30)
for x,y in [(1,100), (2, 200), (3, 300)]:
    print('x = ', x)
    print('y = ', y)
    print('.' * 10)


print('-' * 30)
for c in 'HELLO WORLD!':
    print(c, end=', ')
