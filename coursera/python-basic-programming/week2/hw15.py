# Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел:
# 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

# Формат ввода
# Вводятся три целых числа.

# Формат вывода
# Выведите ответ на задачу.

a, b, c = int(input()), int(input()), int(input())

if a == c and a == c and b == c:
    s = 3
elif a != b and a != c and b != c:
    s = 0
else:
    s = 2
print(s)
