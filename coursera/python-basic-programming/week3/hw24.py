# Дана строка.
# Получите новую строку, вставив между каждыми двумя символами исходной строки символ *.
# Выведите полученную строку.

s = input()

print('*'.join(s[::1]))
