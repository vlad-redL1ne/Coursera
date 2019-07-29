# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите значение второго по величине элемента в этой последовательности,
# то есть элемента, который будет наибольшим, если из последовательности удалить одно вхождение наибольшего элемента.

# Формат ввода
# Вводится последовательность целых чисел,
# оканчивающаяся числом 0 (само число 0 в последовательность не входит, а служит как признак ее окончания).

# Формат вывода
# Выведите ответ на задачу.

arr = []

while True:
    value = int(input())
    if value != 0:
        arr.append(value)
    else:
        break

arr.sort(reverse=True)
print(arr[1])
