# Даны два действительных числа x и y.
# Проверьте, принадлежит ли точка с координатами (x,y) заштрихованному квадрату (включая его границу).
# Если точка принадлежит квадрату, выведите слово YES, иначе выведите слово NO.
# На рисунке сетка проведена с шагом 1.
# http://joxi.ru/Vrw4gBdcOwzb6m


def isPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


print('YES' if isPointInSquare(float(input()), float(input())) else 'NO')
