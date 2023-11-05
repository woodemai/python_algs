def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return comparisons

with open('input.txt', 'r') as file:
    arr = list(map(int, file.readline().strip().split()))

comparisons = insertion_sort(arr)

with open('output.txt', 'w') as file:
    sorted_arr = ' '.join(map(str, arr))
    file.write(f"{sorted_arr}\n")
    file.write(f"{comparisons}")
