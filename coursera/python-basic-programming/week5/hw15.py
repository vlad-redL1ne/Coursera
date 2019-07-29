# Найдите наибольшее значение в списке и индекс последнего элемента,
# который имеет данное значение за один проход по списку,
# не модифицируя этот список и не используя дополнительного списка.


def getLastMaxElement(sequence):
    l = list(map(int, sequence.split()))
    index = 0
    value = l[0]
    for ind, val in enumerate(l):
        if val > value or val == value:
            index, value = ind, val
    print(value, index)


getLastMaxElement(input())
