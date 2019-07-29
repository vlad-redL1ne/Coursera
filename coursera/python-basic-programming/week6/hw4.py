# В обувном магазине продается обувь разного размера.
# Известно, что одну пару обуви можно надеть на другую, если она хотя бы на три размера больше.
# В магазин пришел покупатель.
# Требуется определить, какое наибольшее количество пар обуви сможет предложить ему продавец так,
# чтобы он смог надеть их все одновременно.


def f(size, sizes):
    sizes = list(map(int, sizes.split()))

    count = 0
    for i in sorted(set(sizes)):
        if i == size or i - 3 >= size:
            count += 1
            size = i

    return count


print(f(int(input()), input()))

# a = f(60, '60 63')
# e = 2
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = f(26, '30 35 40 41 42')
# e = 3
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = f(43, '43')
# e = 1
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
