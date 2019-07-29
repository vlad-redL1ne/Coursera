# По данным числам n и k (0≤k≤n) вычислите C из n по k.
# Решение оформите в виде функции C(n, k).
# Для решения используйте рекуррентное соотношение:
# C(n,k) = C(n-1, k-1) + C(n-1, k)

# И равенства:
# С(n, 1)=n
# C(n, n)=1

def C(n, k):
    if n == k or k == 0:
        return 1
    if k == 1:
        return n

    return C(n - 1, k) + C(n - 1, k - 1)


print(C(int(input()), int(input())))
