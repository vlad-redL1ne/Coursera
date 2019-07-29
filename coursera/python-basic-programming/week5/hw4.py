# По данному натуральном n вычислите сумму 1²+2²+3²+...+n².

def squareSumSeq(v):
    return sum(i ** 2 for i in range(1, v + 1))


print(squareSumSeq(int(input())))
