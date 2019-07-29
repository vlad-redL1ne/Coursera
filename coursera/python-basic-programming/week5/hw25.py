# Дан список из чисел и индекс элемента в списке k.
# Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.


def popItemByIndex(items, index):
    arr = list(map(str, items.split()))
    arr.pop(index)
    return ' '.join(arr)


print(popItemByIndex(input(), int(input())))

# a = popItemByIndex('7 6 5 4 3 2 1', 2)
# e = '7 6 4 3 2 1'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
#
# actual = popItemByIndex('4 6 2 4 3 5 12 24 3 5', 4)
# expected = '4 6 2 4 5 12 24 3 5'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
