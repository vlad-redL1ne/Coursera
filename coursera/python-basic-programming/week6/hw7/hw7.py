def f():
    file = open('input.txt', 'r', encoding='utf8')

    studens = {}

    for i in file:
        
        studens[str(i.rsplit(None, 2))[:1]] = i.rsplit(None, 2)[:2]
        print(studens)


f()
