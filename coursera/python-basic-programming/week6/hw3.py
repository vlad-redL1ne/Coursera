# Отсортируйте данный массив, используя встроенную сортировку.


def sort(n):
    return sorted(list(input().split()), key=int)


print(*sort(int(input())))
