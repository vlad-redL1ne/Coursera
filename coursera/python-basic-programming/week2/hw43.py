# TODO

value = int(input())
current_len = 1
max_len = 1

while value != 0:
    prev = value
    value = int(input())
    if value == 0:
        break

    if value > prev:
        current_len += 1
        if current_len > max_len:
            max_len = current_len

    elif value < prev:
        current_len = 0
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    else:
        current_len = 1

print(max_len)
