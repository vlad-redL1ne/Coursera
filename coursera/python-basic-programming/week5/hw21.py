# Выведите значение наименьшего из всех положительных элементов в списке.
# Известно, что в списке есть хотя бы один положительный элемент,
# а значения всех элементов списка по модулю не превосходят 1000.


def getMinPositiveElement(items):
    arr = list(map(int, items.split()))
    minItem = 1000
    for i in arr:
        if 0 < i < minItem:
            minItem = i
    return minItem


print(getMinPositiveElement(input()))
