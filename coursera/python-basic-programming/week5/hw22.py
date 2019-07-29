# Выведите значение наименьшего нечетного элемента списка,
# гарантируется, что хотя бы один нечётный элемент в списке есть.

def getMinOddItem(items):
    arr = list(map(int, items.split()))
    minItem = float('inf')
    for i in range(len(arr)):
        if arr[i] % 2 and arr[i] < minItem:
            minItem = arr[i]

    return minItem


print(getMinOddItem(input()))
