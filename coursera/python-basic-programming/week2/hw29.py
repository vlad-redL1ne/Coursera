# По данному натуральному n вычислите сумму 1²+2²+3²+...+n².

value = int(input())

i = 1
s = 0
while i <= value:
    s += i ** 2
    i += 1

print(s)
