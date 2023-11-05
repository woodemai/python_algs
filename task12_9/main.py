def calculate_determinant(matrix):
    size = len(matrix)
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for j in range(size):
            submatrix = []
            for i in range(1, size):
                submatrix.append(matrix[i][:j] + matrix[i][j+1:])
            submatrix_determinant = calculate_determinant(submatrix)
            determinant += (-1) ** j * matrix[0][j] * submatrix_determinant
        return determinant

matrix = []
with open('input.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        matrix.append(row)

determinant = calculate_determinant(matrix)
with open('output.txt', 'w') as file:
    file.write(str(determinant))
