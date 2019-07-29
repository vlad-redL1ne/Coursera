# Дано четырехзначное число. Определите, является ли его десятичная запись симметричной.
# Если число симметричное, то выведите 1, иначе выведите любое другое целое число.
# Число может иметь меньше четырех знаков, тогда нужно считать,
# что его десятичная запись дополняется слева незначащими нулями.

nnn = int(input())
k1 = 1
k2 = 2
k3 = 3
n3 = (nnn // 10 ** k1) % 10
n2 = (nnn // 10 ** k2) % 10
n1 = (nnn // 10 ** k3) % 10
n4 = (nnn % 10 ** k1)
if n1 == n4 and n2 == n3:
    print(1)
else:
    print(2)
