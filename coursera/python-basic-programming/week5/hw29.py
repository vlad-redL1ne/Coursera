# Дан список, упорядоченный по неубыванию элементов в нем.Определите, сколько в нем различных элементов.


def getUniqueItemsCount(items):
    return len(set(items.split()))


print(getUniqueItemsCount(input()))

# a = getUniqueItemsCount('1 2 2 3 3 3')
# e = 3
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = getUniqueItemsCount('1 2 3 4 5')
# e = 5
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = getUniqueItemsCount('1 1 1 1 1')
# e = 1
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
