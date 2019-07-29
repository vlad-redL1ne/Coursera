# Даны два натуральных числа n и m.
# Сократите дробь (n / m), то есть выведите два других числа p и q таких,
# что (n / m) = (p / q) и дробь (p / q) — несократимая.
# Решение оформите в виде функции ReduceFraction(n, m),
# получающая значения n и m и возвращающей кортеж из двух чисел (return p, q).


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def ReduceFraction(n, m):
    k = gcd(n, m)
    return n // k, m // k


x, y = ReduceFraction(int(input()), int(input()))
print(x, y)
