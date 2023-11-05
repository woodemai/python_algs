import random


def sequential_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return comparisons
    return comparisons


def binary_search(arr, target):
    comparisons = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return comparisons


def interpolation_search(arr, target):
    comparisons = 0
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        comparisons += 1
        if arr[pos] == target:
            return comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return comparisons


def calculate_average_comparisons(search_function, arr):
    total_comparisons = 0
    for i in range(1, len(arr) + 1):
        comparisons = search_function(arr, i)
        total_comparisons += comparisons
    average_comparisons = total_comparisons / len(arr)
    return average_comparisons


with open('input.txt', 'r') as file:
    arr = list(map(int, file.readline().strip().split()))

average_comparisons = calculate_average_comparisons(sequential_search, arr)
with open('output.txt', 'w') as file:
    file.write(f"Среднее число сравнений (последовательный поиск): {average_comparisons}\n")

arr.sort()

average_comparisons = calculate_average_comparisons(binary_search, arr)

with open('output.txt', 'a') as file:
    file.write(f"Среднее число сравнений (двоичный поиск): {average_comparisons}\n")

average_comparisons = calculate_average_comparisons(interpolation_search, arr)
with open('output.txt', 'a') as file:
    file.write(f"Среднее число сравнений (интерполяционный поиск): {average_comparisons}\n")
