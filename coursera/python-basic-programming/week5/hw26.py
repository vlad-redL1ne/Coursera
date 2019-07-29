# Дан список целых чисел, число k и значение C.
# Необходимо вставить в список на позицию с индексом k элемент, равный C,
# сдвинув все элементы, имевшие индекс не менее k, вправо.


def insertByIndex(items, values):
    arr = list(items.split())
    values = list(map(int, values.split()))
    index, value = values[0], values[1]
    arr = arr[:index] + [value] + arr[index:]
    return ' '.join(map(str, arr))


print(insertByIndex(input(), input()))
# a = insertByIndex('7 6 5 4 3 2 1', '2 0')
# e = '7 6 0 5 4 3 2 1'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
#
# a = insertByIndex('4 6 2 4 3 5 12 24 3 5', '4 22')
# e = '4 6 2 4 22 3 5 12 24 3 5'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
