# Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂.
# Определите, можно ли разместить одну из этих коробок внутри другой, при условии,
# что поворачивать коробки можно только на 90 градусов вокруг ребер.

# Формат ввода
# Программа получает на вход числа A₁,B₁,C₁,A₂,B₂,C₂.

# Формат вывода
# Программа должна вывести одну из следующих строчек:
# Boxes are equal, если коробки одинаковые,
# The first box is smaller than the second one, если первая коробка может быть положена во вторую,
# The first box is larger than the second one, если вторая коробка может быть положена в первую,
# Boxes are incomparable, во всех остальных случаях.


a, b, c = int(input()), int(input()), int(input())
x, y, z = int(input()), int(input()), int(input())
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x
if a == x and b == y and c == z:
    print('Boxes are equal')
elif a <= x and b <= y and c <= z:
    print('The first box is smaller than the second one')
elif a >= x and b >= y and c >= z:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
