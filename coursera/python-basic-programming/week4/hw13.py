# Напишите рекурсивную функцию sum(a, b), возвращающуюсумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаютсятолько +1 и -1. Также нельзя использовать циклы.


def sum(a, b):
    return sum(a + 1, b - 1) if b > 0 else a


print(sum(int(input()), int(input())))
