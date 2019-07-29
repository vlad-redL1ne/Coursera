# Дан список чисел.
# Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
# Если наибольших элементов несколько, выведите индекс первого из них.

def getMaxItemFromList(items):
    arr = list(map(int, items.split()))
    maxItem = arr[0]
    maxIndex = 0
    for i in range(1, len(arr)):
        if arr[i] > maxItem:
            maxItem = arr[i]
            maxIndex = i

    print(maxItem, maxIndex)


getMaxItemFromList(input())
