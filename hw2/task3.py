#task3
import numpy as np


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            det += ((-1) ** i) * matrix[0][i] * determinant([row[:i] + row[i + 1:] for row in (matrix[1:])])
        return det


matrix_nxn = [
    [4, 5, 6, 5, 11],
    [1, 4, 2, 0, 13],
    [1, 1, 0, -1, 5],
    [3, 2, 3, 0, 7],
    [4, 1, 2, 3, 8]
]

det = determinant(matrix_nxn)
np_det = np.linalg.det(np.array(matrix_nxn))

print(f"Матрица: {matrix_nxn}")
print(f"Дискриминант матрицы: {det}")
print(f"Дискриминант матрицы с помощью NumPy: {np_det}")