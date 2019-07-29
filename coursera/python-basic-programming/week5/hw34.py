# Дан список, заполненный произвольными целыми числами.
# Найдите в этом списке два числа, произведение которых максимально.
# Выведите эти числа в порядке неубывания.


def getMaxMultiplication(items):
    def multilplicateList(l):
        m = 1
        for x in l:
            m *= x
        return m

    multiplicationCount = 2
    items = list(map(int, items.split()))
    if len(items) <= multiplicationCount:
        return items

    sortedItems = sorted(items)
    positiveItems = sortedItems[-multiplicationCount:]
    negativeItems = sortedItems[:multiplicationCount]

    if multilplicateList(positiveItems) > multilplicateList(negativeItems):
        return positiveItems
    else:
        return negativeItems


print(*getMaxMultiplication(input()))

# a = ' '.join(map(str, getMaxMultiplication('4 3 5 2 5')))
# e = '5 5'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = ' '.join(map(str, getMaxMultiplication('-4 3 -5 2 5')))
# e = '-5 -4'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
