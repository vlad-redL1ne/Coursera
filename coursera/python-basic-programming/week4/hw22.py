# TODO to be done

def squareble(value):
    if value ** 0.5 % 1 == 0:
        return True


def squaresOnly(sq=False):
    v = int(input())
    if v == 0:
        return
    else:
        squaresOnly()
        if squareble(v):
            sq = True
            print(v)

    if not sq:
        print(0)


squaresOnly()
