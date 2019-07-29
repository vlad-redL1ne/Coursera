# Дан список.
# Не изменяя его и не используя дополнительные списки, определите,
# какое число в этом списке встречается чаще всего.
# Если таких чисел несколько, выведите любое из них.


def popular_item(items):
    items = list(items.split())

    popular_item = items[0]
    popular_count = items.count(popular_item)

    for i in items:
        count = items.count(i)
        if count > popular_count:
            popular_item, popular_count = i, count

    return popular_item


print(popular_item(input()))

# a = popular_item('1 2 3 2 3 3')
# e = '3'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)

# a = popular_item('1 2 3 4 5 6 7 8 9 1')
# e = '1'
# assert (a == e), '--> actual: %s, expected %s' % (a, e)
