def greaterThanNeighbourhoods(items):
    arr = list(map(int, items.split()))
    count = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count += 1
    return count


print(greaterThanNeighbourhoods(input()))
