# Дано действительное положительное число a и целое неотрицательное число n.
# Вычислите aⁿ, не используя циклы и стандартную функцию pow,
# но используя рекуррентное соотношение aⁿ=a⋅aⁿ⁻¹.
# Решение оформите в виде функции power(a, n) (которая возвращает aⁿ).


def power(a, n):
    return a * power(a, n - 1) if n >= 1 else 1


print(power(float(input()), int(input())))
