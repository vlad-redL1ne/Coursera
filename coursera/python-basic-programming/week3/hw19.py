# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти словаместами.
# Результат запишите в строку и выведите получившуюся строку.
# При решении этой задачи нельзя пользоваться циклами и инструкцией if.

s = input()

print(s[s.rindex(' ') + 1:], s[:s.index(' ')])
