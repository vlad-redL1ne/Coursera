# По данному натуральному n вычислите сумму 1!+2!+3!+...+n!.
# В решении этой задачи можно использовать только один цикл.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factiorialsSumm(x):
    return sum([factorial(i) for i in range(1, x + 1)])


print(factiorialsSumm(int(input())))
