# На склад, который имеет форму прямоугольного параллелепипеда, привезли ноутбуки, упакованные в коробки.
# Каждая коробка также имеет форму прямоугольного параллелепипеда.
# По правилам хранения коробки с ноутбуками должны быть размещены на складе с выполнением следующих двух условий:

# Стороны коробок должны быть параллельны сторонам склада.
# Коробку при помещении на склад разрешается расположить где угодно (с выполнением предыдущего условия),
# в том числе на другой коробке, но все коробки должны быть ориентированы одинаково
# (т.е. нельзя одну коробку расположить “стоя”, а другую —“лежа”)
# Напишите программу, которая по размерам склада и размерам коробки с ноутбуком определит
# максимальное количество ноутбуков, которое может быть размещено на складе.

# Формат ввода
# Программа получает на вход шесть натуральных чисел.
# Первые три задают длину, высоту и ширину склада.
# Следующие три задают соответственно длину, высоту и ширину коробки с ноутбуком.

# Формат вывода
# Программа должна вывести одно число — максимальное количество ноутбуков, которое может быть размещено на складе.

a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
z = int(input())

arr = [int(a // x) * int(b // y) * int(c // z),
       int(a // y) * int(b // x) * int(c // z),
       int(a // x) * int(b // z) * int(c // y),
       int(a // z) * int(b // x) * int(c // y),
       int(a // z) * int(b // y) * int(c // x),
       int(a // y) * int(b // z) * int(c // x)]

arr.sort(reverse=True)
print(arr[0])
