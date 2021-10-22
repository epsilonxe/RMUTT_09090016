print('DIVISOR CALCULATOR')
try:
    x = float(input('Enter x = '))
    y = float(input('Enter y = '))
    z = x / y
    print(f'{x}/{y} = {z}')
except ZeroDivisionError:
    z = None
    print('y must NOT be zero')
except ValueError:
    print('x and y must be numeric')
except:
    z = None
    print('ERROR: UNKNOWN ERROR!')
