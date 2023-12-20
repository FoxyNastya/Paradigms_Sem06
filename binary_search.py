def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


numbers = [1, 2, 3, 4, 5]
target = 4
result = binary_search(numbers, target)

if result == -1:
    print("Элемент не найден")
else:
    print(f"Элемент располагается по индексу {result}")
