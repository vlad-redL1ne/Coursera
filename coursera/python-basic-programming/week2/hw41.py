# Переставьте цифры числа в обратном порядке .

# Формат ввода
# Задано единственное число N

# Формат вывода
# Необходимо вывести цифры данного числа в обратном порядке.

value = int(input())
reversed_value = 0

while value > 0:
    digit = value % 10
    value //= 10
    reversed_value *= 10
    reversed_value += digit

print(reversed_value)
