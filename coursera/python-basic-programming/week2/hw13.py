# Даны три целых числа A, B, C. Определить, есть ли среди них хотя бы одно четное и хотя бы одно нечетное.

# Формат ввода
# Числа A, B, C, не превышающие по модулю 10000.

# Формат вывода
# Одна строка – "YES" или "NO".

a = int(input())
b = int(input())
c = int(input())

even = False
odd = False

if (a % 2 == 1) or (b % 2 == 1) or (c % 2 == 1):
    odd = True

if (a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0):
    even = True

print('YES' if even and odd else 'NO')
