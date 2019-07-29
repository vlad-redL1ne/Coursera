# Напишите программу, которая находит в массиве элемент, самый близкий по величине к данному числу.
#
# Формат ввода
#
# В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива.
# Во второй строке содержатся N чисел – элементы массива (целые числа, не превосходящие по модулю 1000).
# В третьей строке вводится одно целое число x, не превосходящее по модулю 1000.


def getClosestToValue(itemsLen, items, value):
    items = list(map(int, items.split()))
    return min(items, key=lambda x: abs(x - value))


print(getClosestToValue(int(input()), input(), int(input())))

# a = getClosestToValue('5', '1 2 3 4 5', 6)
# e = 5
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
