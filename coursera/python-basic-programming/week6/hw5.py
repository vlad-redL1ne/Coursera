# Системный администратор вспомнил, что давно не делал архива пользовательских файлов.
# Однако, объем диска, куда он может поместить архив, может быть меньше чем суммарный объем архивируемых файлов.

# Известно, какой объем занимают файлы каждого пользователя.

# Напишите программу, которая по заданной информации о пользователях и свободному объему
# на архивном диске определит максимальное число пользователей, чьи данные можно поместить в архив.


def f(values):
    available_size, users_count = map(int, values.split())
    sizes = sorted([int(input()) for _ in range(users_count)])
    sizes_sum = sum(sizes)
    while sizes_sum > available_size and users_count:
        sizes_sum -= sizes.pop()
        users_count -= 1

    return users_count


print(f(input()))
