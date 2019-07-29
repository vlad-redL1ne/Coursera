# Даны два целых числа A и B (при этом A≤B). Выведите все числа от A до B включительно.

def printRange(a, b):
    print(*(range(a, b + 1)))


printRange(int(input()), int(input()))
