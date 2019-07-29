# Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
# Если соседних элементов одного знака нет - не выводите ничего.
# Если таких пар соседей несколько - выведите первую пару.

def getNeighbourValues(items):
    arr = list(map(int, items.split()))
    for i in range(1, len(arr)):
        if (arr[i - 1] > 0 and arr[i] > 0) or (arr[i - 1] < 0 and arr[i] < 0):
            print(arr[i - 1], arr[i])
            break


getNeiborValues(input())
