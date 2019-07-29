# Даны три стороны треугольника a,b,c.
# Определите тип треугольника с заданными сторонами.
# Выведите одно из четырех слов: rectangular для прямоугольного треугольника, acute для остроугольного треугольника,
# obtuse для тупоугольного треугольника или impossible, если треугольника с такими сторонами не существует.

import math

a = int(input())
b = int(input())
c = int(input())
a, b, c = sorted([a, b, c])
if a + b <= c:
    print('impossible')
elif c == math.sqrt((a ** 2) + (b ** 2)):
    print('rectangular')
elif ((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b) > 0:
    print('acute')
else:
    print('obtuse')
