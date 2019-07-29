# Шоколадка имеет вид прямоугольника, разделенного на n×m долек.
# Шоколадку можно один раз разломить по прямой на две части.
# Определите, можно ли таким образом отломить от шоколадки ровно k долек.
# Формат ввода
# Программа получает на вход три числа: n, m, k
# Формат вывода
# Программа должна вывести одно из двух слов: YES или NO.

n = int(input())
m = int(input())
k = int(input())

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
