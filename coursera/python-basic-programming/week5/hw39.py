# Дан список целых чисел.
# Требуется “сжать” его, переместив все ненулевые элементы в левую часть списка,
# не меняя их порядок, а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя,
# дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
# Распечатайте полученный список.


def shift_array(items):
    items = list(map(int, items.split()))

    zero_index = 9223372036854775807

    for i in range(0, len(items)):
        if items[i] == 0:
            if i < zero_index:
                zero_index = i

        elif i > zero_index:
            items[zero_index], items[i] = items[i], 0
            zero_index += 1

    return items


print(*shift_array(input()))

# a = shift_array('4 0 5 0 3 0 0 5')
# e = [4, 5, 3, 5, 0, 0, 0, 0]
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = shift_array('0 0 0 0 0 0 0 0 0 1')
# e = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
