def circle_area(radius, pi=3.14):
    area = pi * radius * radius
    return area


def circle_area_v2(radius=0, pi=3.14):
    area = pi * radius * radius
    return area

x = 10
print(circle_area(x, 3.14))
print(circle_area(x))
print(circle_area(x, 3.1415))
print(circle_area(x, 3.14159265))
print(circle_area(x, pi=3.14159265))


print(circle_area_v2())
print(circle_area_v2(10, 3.1415))
print(circle_area_v2(radius=10, pi=3.1415))
print(circle_area_v2(pi=3.1415, radius=x))
