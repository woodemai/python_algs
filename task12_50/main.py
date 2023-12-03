from itertools import permutations


def quicksort_comparisons(arr):
    comparisons = 0

    def partition(arr, low, high):
        nonlocal comparisons
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort(arr, low, high):
        nonlocal comparisons
        if low < high:
            pi = partition(arr, low, high)
            quicksort(arr, low, pi - 1)
            quicksort(arr, pi + 1, high)

    quicksort(arr, 0, len(arr) - 1)
    return comparisons


def read_N_from_file(filename):
    with open(filename, 'r') as file:
        return int(file.readline().strip())


def generate_and_find_max_comparisons(N):
    all_arrays = list(permutations(range(1, N + 1)))
    max_comparisons = 0
    max_comparisons_array = []

    for array in all_arrays:
        comparisons = quicksort_comparisons(list(array))
        if comparisons > max_comparisons:
            max_comparisons = comparisons
            max_comparisons_array = list(array)

    return max_comparisons_array, max_comparisons


def write_result_to_file(filename, array, comparisons):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, array)) + '\n')
        file.write(str(comparisons) + '\n')


input_file = 'input.txt'
N = read_N_from_file(input_file)
result_array, result_comparisons = generate_and_find_max_comparisons(N)
write_result_to_file('output.txt', result_array, result_comparisons)
