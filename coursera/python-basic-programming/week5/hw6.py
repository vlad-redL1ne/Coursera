# Дано несколько чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.

def getZeroEqualsNums(n):
    return [int(input()) for _ in range(n)].count(0)

print(getZeroEqualsNums(int(input())))
