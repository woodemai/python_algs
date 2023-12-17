from itertools import permutations


def quicksort_comparisons_and_swaps(arr):
    comparisons = 0
    swaps = 0

    def partition(arr, low, high):
        nonlocal comparisons, swaps
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1

    def quicksort(arr, low, high):
        nonlocal comparisons, swaps
        if low < high:
            pi = partition(arr, low, high)
            quicksort(arr, low, pi - 1)
            quicksort(arr, pi + 1, high)

    quicksort(arr, 0, len(arr) - 1)
    return comparisons, swaps


def read_N_from_file(filename):
    with open(filename, 'r') as file:
        return int(file.readline().strip())


def generate_and_find_max_comparisons_and_swaps(N):
    all_arrays = list(permutations(range(1, N + 1)))
    max_comparisons = 0
    max_swaps = 0
    max_comparisons_arrays = []

    for array in all_arrays:
        comparisons, swaps = quicksort_comparisons_and_swaps(list(array).copy())
        if comparisons > max_comparisons:
            max_comparisons = comparisons
            max_swaps = swaps
            max_comparisons_arrays = list(array)
        elif comparisons == max_comparisons and swaps > max_swaps:
            max_swaps = swaps
            max_comparisons_arrays = list(array)

    return max_comparisons_arrays, max_comparisons, max_swaps


def write_result_to_file(filename, array, comparisons, swaps):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, array)) + '\n')
        file.write(f"{comparisons} comparisons\n")
        file.write(f"{swaps} swaps\n")


input_file = 'input.txt'
N = read_N_from_file(input_file)
result_arrays, result_comparisons, result_swaps = generate_and_find_max_comparisons_and_swaps(N)
write_result_to_file('output.txt', result_arrays, result_comparisons, result_swaps)
