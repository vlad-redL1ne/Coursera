# Возводить в степень можно гораздо быстрее, чем за n умножений!
# Для этого нужно воспользоваться следующими рекуррентными соотношениями:
# aⁿ = (a²)ⁿ/² при четном n, aⁿ=a⋅aⁿ⁻¹ при нечетном n.
# Реализуйте алгоритм быстрого возведения в степень.
# Если вы все сделаете правильно,то сложность вашего алгоритма будет O(logn).


def power(a, n):
    if n == 0:
        return 1
    if n % 2:
        return power(a, n - 1) * a
    else:
        return power(a * a, n / 2)


print(power(float(input()), float(input())))
