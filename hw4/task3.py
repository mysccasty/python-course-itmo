# task3

import numpy as np

matrix_a = np.random.rand(10, 10)
print("Сгенерированная матрица A:\n", matrix_a)

determinant = np.linalg.det(matrix_a)
if np.isclose(determinant, 0):
    print("Матрица вырождена. Определитель равен 0.")
else:
    print("Определитель матрицы A:", determinant)

transposed_matrix = np.transpose(matrix_a)
print("Транспонированная матрица A:\n", transposed_matrix)

rank = np.linalg.matrix_rank(matrix_a)
print("Ранг матрицы A:", rank)

eigenvalues, eigenvectors = np.linalg.eig(matrix_a)
print("Собственные значения:\n", eigenvalues)
print("Собственные векторы:\n", eigenvectors)

matrix_b = np.random.rand(10, 10)
print("Сгенерированная матрица B:\n", matrix_b)

sum_matrix = matrix_a + matrix_b
print("Сумма матриц A и B:\n", sum_matrix)

product_matrix = np.dot(matrix_a, matrix_b)
print("Произведение матриц A и B:\n", product_matrix)
