# Переставьте элементы данного списка в обратном порядке, затем выведите элементы полученного списка.
# Эта задача отличается от предыдущей тем, что вам нужно изменить значенияэлементов самого списка,
# поменяв местами A[0] c A[n-1],A[1] с A[n-2], а затем вывести элементы списка подряд.


def inReverseOrder(items):
    arr = list(map(int, items.split()))
    n = 1
    l_arr = len(arr)
    while n < l_arr:
        for i in range(l_arr - n):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

        n += 1

    return ' '.join(map(str, arr))


print(inReverseOrder(input()))

# actual = inReverseOrder('1 2 3 4 5')
# expected = '5 4 3 2 1'
# assert (actual == expected), '--> actual: %s, expected %s' % (actual, expected)
#
# actual = inReverseOrder('4 5 3 4 2 3')
# expected = '3 2 4 3 5 4'
# assert (actual == expected), '--> actual: %s, expected %s' % (actual, expected)
