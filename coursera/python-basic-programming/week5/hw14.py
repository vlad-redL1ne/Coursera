# Найдите количество положительных элементов в данном списке.


def getCountPositiveElements(s):
    return len([i for i in map(int, s.split()) if i > 0])


print(getCountPositiveElements(input()))
