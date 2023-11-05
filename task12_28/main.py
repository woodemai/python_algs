def shaker_sort(arr):
    comparisons = 0
    start = 0
    end = len(arr) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1
    return comparisons

with open('input.txt', 'r') as file:
    arr = list(map(int, file.readline().strip().split()))

comparisons = shaker_sort(arr)

with open('output.txt', 'w') as file:
    sorted_arr = ' '.join(map(str, arr))
    file.write(f"{sorted_arr}\n")
    file.write(f"{comparisons}")
