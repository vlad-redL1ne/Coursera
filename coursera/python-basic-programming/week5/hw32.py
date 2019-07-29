# Выведите все четные элементы списка.


def getEvenItems(items):
    return [x for x in list(map(int, items.split())) if not x % 2]


print(*getEvenItems(input()))

# a = ' '.join(map(str, (getEvenItems('1 2 2 3 3 3 4'))))
# e = '2 2 4'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = ' '.join(map(str, (getEvenItems('1 2 3 4 5'))))
# e = '2 4'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
