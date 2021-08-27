my_list = []
print('my_list = ', my_list)
round = 0
while round < 5:
    n = float(input('Enter a number: '))
    my_list.append(n)
    print('Now my_list = ', my_list)
    round = round + 1
print('Summation =', sum(my_list))

i = 0
while i < 5:
    print('my_list at index', i, '=', my_list[i])
    i = i + 2
