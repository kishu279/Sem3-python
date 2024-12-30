# take input from user a mxn array and generate another matrix of nxm 1 to 20 and perform  matrixa x matrixb and the print the matrix c
from numpy import *

rowsA = 4
colsA = 3

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element at position ({i+1}, {j+1}): ")))
        matrix.append(row)
    return matrix

matrixA = input_matrix(rowsA, colsA)

matrixB = random.randint(21, size=(colsA, rowsA))

res = dot(matrixA, matrixB)

print(f"Matrix A: {matrixA}")
print(f"Matrix B: {matrixB}")
print(f"Result of matrix multiplication (A dot B): {res}")