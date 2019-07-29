# Даны два действительных числа x и y.
# Проверьте, принадлежит ли точка с координатами(x,y) заштрихованному квадрату (включая его границу).
# Если точка принадлежит квадрату, выведите слово YES,иначе выведите слово NO.
# На рисунке сетка проведена с шагом 1.
# http://joxi.ru/MAj4Yyqc4wGENm

def isPointInSquare(x, y):
    x1, y1 = -1, -1
    x2, y2 = 1, 1

    byX = x1 <= x <= x2
    byY = y1 <= y <= y2
    bySum = abs(x) + abs(y) <= 1

    return byX and byY and bySum


print('YES' if isPointInSquare(float(input()), float(input())) else 'NO')
