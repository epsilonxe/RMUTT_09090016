# Functions

# Type: No-Input/No-Output

def showline():
    print('-' * 45)
    print('-' * 45)

# -------------------------------------

# Type: One-Input (One Argument) /No-Output

def showline_aaa(n):
    print('-' * n)

# -------------------------------------

# Type: Multiple-Input/ No-Output

def showline_bbb(chr, n):
    print(chr * n)
    print(chr * n)

# ------------------------------------

# Type: One-Input/One-Output

'''
            |-----|
INPUT -->   |  F  | --> OUTPUT
(ARGUMENT)  |-----|     (RETURN)

'''

def circle_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

def circle_circumference(radius):
    pi = 3.14
    circumference = 2 * pi * radius
    return circumference

# -----------------------------------

# Type: One-Input/Multiple-Output:

def circle_calculation(radius):
    area = circle_area(radius)
    circ = circle_circumference(radius)
    return (area, circ)

# --------------------------------------

# Type: Multiple-Input/Multiple-Output:

def rectangle_calculation(width, height):
    area = width * height
    perimeter = 2 * width + 2 * height
    return area, perimeter


# Main Program
print('Hello World!')
showline()
print('My name is Dear')
showline_aaa(80)
showline_aaa(10)
print('Test something here')
showline_bbb('#', 60)
showline_bbb('*', 15)

x = circle_area(10)
print('Area of a circle is', x)
# print('Area of a circle is', circle_area(10))
y = circle_circumference(10)
print('Circumference of a circle is', y)

z_area, z_circ = circle_calculation(10)
# print('Calculation of a circle is', z)
print(z_area)
print(z_circ)

rect_area, rect_per = rectangle_calculation(4, 5)
print('Area of a rectangle is', rect_area)
print('Perimeter of a rectangle is', rect_per)