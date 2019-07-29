# Дан список чисел.
# Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.


def getEqualPairs(items):
    items = list(map(int, items.split()))
    items_len = len(items)
    count = 0

    for i in range(items_len):
        for j in range(i + 1, items_len):
            if items[i] == items[j]:
                count += 1

    return count


print(getEqualPairs(input()))

# a = getEqualPairs('1 2 3 2 3')
# e = 2
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = getEqualPairs('1 1 1 1 1')
# e = 10
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
