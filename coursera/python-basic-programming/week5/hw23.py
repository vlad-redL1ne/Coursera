# Выведите элементы данного списка в обратном порядке, не изменяя сам список.


def inReverseOrder(items):
    return ' '.join(list(map(str, items.split()))[::-1])


print(inReverseOrder(input()))
