# В данном списке из n≤10⁵ целых чисел найдите три числа,произведение которых максимально.
# Решение должно иметь сложность O(n), где n - размер списка.
# Выведите три искомых числа в любом порядке.


def getMaxMultiplication(items):
    def multilplicateList(l):
        m = 1
        for x in l:
            m *= x
        return m

    multiplicationCount = 3

    items = list(map(int, items.split()))
    lenItems = len(items)
    if lenItems <= multiplicationCount:
        return items

    sortedItems = sorted(items)
    positiveItems = sortedItems[-multiplicationCount:]
    negativeItems = sortedItems[:multiplicationCount - 1]
    negativeItems.append(positiveItems[multiplicationCount - 1])

    if multilplicateList(positiveItems) > multilplicateList(negativeItems):
        return positiveItems
    else:
        return negativeItems


print(*getMaxMultiplication(input()))

# a = ' '.join(map(str, getMaxMultiplication('3 5 1 7 9 0 9 -3 10')))
# e = '9 9 10'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = ' '.join(map(str, getMaxMultiplication(
#     '23 16 7 -33 43 -3 -26 -29 -25 -40 -16 -17 -23 27 55 -34 37 18 -50 51'
#     '46 37 25'
#     '25 24 -32 -38 -8 -52 -8 49 0 47 -54 27 -1 6 30 37 -27 -20 -37 -35 -42'
#     '9 36 -39 45')))
# e = '-54 -52 55'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
