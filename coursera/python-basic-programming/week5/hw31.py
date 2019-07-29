# Циклически сдвиньте элементы списка вправо(
# A[0] переходит на место A[1], A[1] на место A[2], ...,
# последний элемент переходит на место A[0]).


def cycleShift(items):
    items = list(items.split())
    itemsLen = len(items)

    last = items[itemsLen - 1]
    for i in range(itemsLen - 1, 0, -1):
        items[i], items[i - 1] = items[i - 1], items[i]

    items[0] = last

    return items


print(*cycleShift(input()))

# a = cycleShift('1 2 3 4 5')
# e = '5 1 2 3 4'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = cycleShift('4 5 3 4 2 3')
# e = '3 4 5 3 4 2'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
