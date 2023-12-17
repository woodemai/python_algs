import math

w = 5


def insertion_sort(arr, left, right):
    for i in range(left, right):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def swap(a, b):
    temp = a
    a = b
    b = temp


def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

def partition(list, left, right):




def select_opt(list, k, left, right):
    while True:
        d = right - left + 1
        if d <= w:
            insertion_sort(list, left, right)
            result = left + k - 1
            break
    dd = math.floor(d / w)
    for i in range(1, dd):
        insertion_sort(list, left + (i - 1) * w, left + i * w - 1)
        (
            list[left + i - 1],
            list[left + (i - 1) * w + math.ceil(w / 2) - 1]) = (
            list[left + (i - 1) * w + math.ceil(w / 2) - 1],
            list[left + i - 1]
        )

    v = select_opt(list, math.ceil(dd / 2), left, left + dd - 1)

    list[left], list[v] = list[v], list[left]
    v = partition(list, left, right)
    temp = v - left + 1
    comparison_result = compare(k, temp)
    if comparison_result == -1:
        right = v - 1
    elif comparison_result == 0:
        result = v
    else:  # comparison_result == +1
        k -= temp
        left = v + 1

arr = [20, 12, 18, 16, 24, 10, 22, 14]
print(select_opt(list, 1, 0, len(list) - 1))