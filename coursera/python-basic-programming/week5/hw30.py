# Переставьте соседние элементы списка (A[0] c A[1],A[2] c A[3] и т.д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.


def mixArray(arr):
    arr = list(arr.split())
    for i in range(1, len(arr), 2):
        arr[i], arr[i - 1] = arr[i - 1], arr[i]

    return arr


print(*mixArray(input()))

# a = mixArray('1 2 3 4 5')
# e = '2 1 4 3 5'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = mixArray('4 5 3 4 2 3')
# e = '5 4 4 3 3 2'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
