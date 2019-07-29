# Дана строка.
# Замение в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.

s = input()

f_h = s.index('h') + 1
l_h = s.rindex('h')
subs = s[f_h:l_h:]

print(s[:f_h] + subs.replace('h', 'H') + s[l_h:])
