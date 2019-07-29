# N кеглей выставили в один ряд, занумеровав их слева направо числами от 1 до N.
# Затем по этому ряду бросили K шаров, при этом i-й шар сбил все кегли с номерами от lᵢ до rᵢ включительно.
# Определите, какие кегли остались стоять на месте.


def get_alive_skittles(items):
    inp = list(map(int, items.split()))
    skittles = ['I' for _ in range(inp[0])]

    for i in range(inp[1]):
        shot = list(map(int, input().split()))
        for j in range(shot[0] - 1, shot[1]):
            skittles[j] = '.'

    return skittles


print(''.join(get_alive_skittles(input())))
