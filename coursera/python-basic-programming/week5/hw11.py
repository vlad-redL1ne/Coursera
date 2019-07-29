# Для настольной игры используются карточки с номерами от 1 до N.Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.


def getLostCardNumber():
    count = int(input())
    totalSum = sum(i for i in range(1, count + 1))
    inputValuesSum = sum(int(input()) for _ in range(1, count))
    return totalSum - inputValuesSum


print(getLostCardNumber())
