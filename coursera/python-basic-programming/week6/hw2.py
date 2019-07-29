# Даны два списка, упорядоченных по возрастанию (каждый список состоит из различных элементов).

# Найдите пересечение множеств элементов этих списков, то есть те числа,
# которые являются элементами обоих списков. Алгоритм должен иметь сложность O(len(A)+len(B)).

# Решение оформите в виде функции Intersection(A, B).
# Функция должна возвращать список пересечения данных списков в порядке возрастания элементов.
# Модифицировать исходные списки запрещается.


def intersection(first, second):
    first = set(first.split())
    second = set(second.split())

    c = first & second
    return sorted(c, key=int)


print(*intersection(input(), input()))

# a = intersection('1 3 4 7 9', '2 3 7 10 11')
# e = list('3 7'.split())
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = intersection('1 4 6 8', '1 4 6 8')
# e = list('1 4 6 8'.split())
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
