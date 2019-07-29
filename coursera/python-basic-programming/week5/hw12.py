# Даны два четырёхзначных числа A и B.
# Выведите все четырёхзначные числа на отрезке от A до B, запись которых является палиндромом.

def getPolindromNumbers(a, b):
    for i in range(a, b + 1):
        if str(i) == str(i)[::-1]:
            print(i)


getPolindromNumbers(int(input()), int(input()))
