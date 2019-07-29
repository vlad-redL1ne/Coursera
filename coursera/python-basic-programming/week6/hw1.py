def merge(a, b):
    first_list = list(map(int, a.split()))
    len_first_list = len(first_list)
    second_list = list(map(int, b.split()))
    len_second_list = len(second_list)

    result_list = []

    i, j = 0, 0
    for k in range(len_first_list + len_second_list):
        if i < len_first_list and j < len_second_list:
            if first_list[i] < second_list[j]:
                result_list.append(first_list[i])
                i += 1
            else:
                result_list.append(second_list[j])
                j += 1
        elif i < len_first_list:
            result_list.append(first_list[i])
            i += 1
        elif j < len_second_list:
            result_list.append(second_list[j])
            j += 1

    return result_list


print(*merge(input(), input()))

# a = merge('1 5 7', '2 4 4 5')
# e = list(map(int, '1 2 4 4 5 5 7'.split()))
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = merge('1 4 7', '1 5 6')
# e = list(map(int, '1 1 4 5 6 7'.split()))
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
