# По данному числу n вычислите сумму 1+(1 / 2²)+(1 / 3²)+...+(1 / n²).

value = float(input())
i = 1
s = 0

while i <= value:
    s += 1 / (i ** 2)
    i += 1

print(s)
