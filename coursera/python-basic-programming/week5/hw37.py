# Дан список.
# Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.


def getUniqueItems(items):
    items = list(items.split())
    return list(filter(lambda i: items.count(i) == 1, items))


print(*getUniqueItems(input()))

# a = getUniqueItems('1 2 2 3 3 3')
# e = ['1']
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = getUniqueItems('4 3 5 2 5 1 3 5')
# e = ['4', '2', '1']
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
