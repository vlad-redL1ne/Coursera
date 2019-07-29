# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

def greaterThanPrevious(values):
    l = list(map(int, values.split()))
    s = ''
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            print(l[i])


greaterThanPrevious(input())
