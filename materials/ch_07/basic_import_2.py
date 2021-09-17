from lab_3 import calculate_bmi as bmi
from lab_3 import bmi_meaning as mbmi


x = 65
y = 1.7
z = bmi(x, y)
result = mbmi(z)
print('BMI =', z, '->', result)