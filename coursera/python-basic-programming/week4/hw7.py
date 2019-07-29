# Если точка принадлежит области (область включает границы), выведите слово YES, иначе выведите слово NO.
# Решение должно содержать функцию IsPointInArea(x, y),
# возвращающую True, если точка принадлежит области и False, если не принадлежит.
# Основная программа должна считать координаты точки, вызвать функцию IsPointInArea
# и в зависимости от возвращенного значения вывести на экран необходимое сообщение.
# Функция IsPointInArea не должна содержать инструкцию if.
# http://joxi.ru/xAeqznMHpeP8OA

def isPointInArea(x, y):
    llr = (x + y >= 0)
    rll = (2 * x - y + 2 <= 0)
    lll = (x + y <= 0)
    rlr = (2 * x - y + 2 >= 0)

    in_circle = isPointInCircle(x, y) and llr and rll
    in_bottom = not isPointInsideCircle(x, y) and lll and rlr

    return in_circle or in_bottom


def isPointInCircle(x, y):
    xc = -1
    yc = 1
    r = 2

    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2


def isPointInsideCircle(x, y):
    xc = -1
    yc = 1
    r = 2

    return (x - xc) ** 2 + (y - yc) ** 2 < r ** 2


x, y = float(input()), float(input())

print('YES' if isPointInArea(x, y) else 'NO')
