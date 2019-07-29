# Назовем число палиндромом, если оно не меняется при перестановке его цифр в обратном порядке.
# Напишите программу, которая по заданному числу K выводит количество натуральных палиндромов, не превосходящих K.

# Формат ввода
# Задано единственное число K (1≤K≤100000).

# Формат вывода
# Необходимо вывести количество натуральных палиндромов, не превосходящих K.

def getReversedValue(value):
    reversed_value = 0
    while value > 0:
        digit = value % 10
        value //= 10
        reversed_value *= 10
        reversed_value += digit
    return reversed_value


value = int(input())
count = 0
i = 1

while i <= value:
    if getReversedValue(i) == i:
        count += 1
    i += 1

print(count)
