def shell_sort(arr, gaps):
    comparisons = 0
    for gap in gaps:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            comparisons += 1
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                comparisons += 1
            arr[j] = temp
    return comparisons


def read_array_from_file(filename):
    with open(filename, 'r') as file:
        return list(map(int, file.readline().split()))


def write_result_to_file(filename, sorted_array, comparisons):
    with open(filename, 'w') as file:
        file.write(' '.join(map(str, sorted_array)) + '\n')
        file.write(str(comparisons) + '\n')


input_filename = 'input.txt'
output_filename = 'output.txt'

array = read_array_from_file(input_filename)

# Сортировка смещениями hs, где hs+1 = 2hs + 1
hs_gaps = [1]
s = 1
while hs_gaps[-1] < len(array) / 2:
    s += 1
    hs_gaps.append(2 ** s - 1)

comparisons_hs = shell_sort(array.copy(), hs_gaps)

# Сортировка смещениями hs, где hs+1 = 3hs + 1
hs_gaps_3 = [1]
s = 1
while hs_gaps_3[-1] < (len(array) * 2 + 1) / 3:
    s += 1
    hs_gaps_3.append(3 ** s - 1)

comparisons_hs_3 = shell_sort(array.copy(), hs_gaps_3)

write_result_to_file(output_filename, array, comparisons_hs + comparisons_hs_3)
