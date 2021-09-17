def area_triangle(w, h):
    area = 0.5 * w * h
    return area

area_triangle_short = lambda x, y: 0.5 * x * y

circle_cal = lambda r: (3.14 * r *r, 2 * 3.14 * r)

print(area_triangle(10, 12))
print(area_triangle_short(10, 12))

print(circle_cal(10))
