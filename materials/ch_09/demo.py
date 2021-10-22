print('TRAIANGLE AREA CALCULATOR')
try:
    b = input('Enter a length of base: ')
    h = input('Enter a length of height: ')
    area = 0.5 * b * h
    print(area)
except TypeError:
    print('Inputs must be integers or floating points')
except:
    print('There are some error!')
    print('Please check it')