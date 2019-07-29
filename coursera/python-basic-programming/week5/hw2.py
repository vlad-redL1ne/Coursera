# Даны два целых числа A и В.
# Выведите все числа от A до B включительно, в порядке возрастания,если A < B, или в порядке убывания в противном случае.

def printRange(a, b):
    r = range(a, b - 1, -1) if a > b else range(a, b + 1)

    for i in r:
        print(i)


printRange(int(input()), int(input()))
