# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.

# Формат ввода
# Вводится целое положительное число.

# Формат вывода
# Выведите ответ на задачу.

value = int(input())

i = 2
while i <= value:
    if value % i == 0:
        print(i)
        break
    i += 1
