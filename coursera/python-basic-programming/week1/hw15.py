# Дано целое число N. Выведите следующее за ним четное число.

value = int(input())
if value % 2 != 0:
    value += 1
else:
    value += 2

print(value)
