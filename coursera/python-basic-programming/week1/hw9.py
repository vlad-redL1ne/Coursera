# Дано трехзначное число. Найдите сумму его цифр.

value = int(input())

print(sum([int(i) for i in str(value)]))
