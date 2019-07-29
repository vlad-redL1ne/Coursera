# В списке все элементы попарно различны.
# Поменяйте местами минимальный и максимальный элемент этого списка.


def shakeMinMaxItems(items):
    items = list(map(int, items.split()))

    minIndex = items.index(min(items))
    maxIndex = items.index(max(items))

    items[minIndex], items[maxIndex] = items[maxIndex], items[minIndex]

    return items


print(*shakeMinMaxItems(input()))

# a = ' '.join(map(str, shakeMinMaxItems('3 4 5 2 1')))
# e = '3 4 1 2 5'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = ' '.join(map(str, shakeMinMaxItems('1 5 4 3 2')))
# e = '5 1 4 3 2'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = ' '.join(map(str, shakeMinMaxItems('-30000 30000')))
# e = '30000 -30000'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
