def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def select_opt(arr, k, low, high):
    if low == high:
        return arr[low]

    pivot_index = partition(arr, low, high)

    length = pivot_index - low + 1

    if length == k:
        return arr[pivot_index]
    elif k < length:
        return select_opt(arr, low, pivot_index - 1, k)
    else:
        return select_opt(arr, pivot_index + 1, high, k - length)


arr = [20, 12, 18, 16, 24, 10, 22, 14]

k1, k2 = 4, 5
res1 = select_opt(arr.copy(), k1, 0, len(arr) - 1)
res2 = select_opt(arr.copy(), k2, 0, len(arr) - 1)
print("Медиана: ", (res1 + res2) / 2)
