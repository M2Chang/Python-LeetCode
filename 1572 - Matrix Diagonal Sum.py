import numpy as np #import the library to create random matrixes

#create the function to return the diagonal sum

def diagonalmatrix(matrix):
    size = len(matrix)
    x = size - 1
    sum = 0
    for i in range(size):
        sum +=matrix[i][i]
        sum +=matrix[i][x] if i!=x else 0
        x -= 1
    return sum


matrix = np.random.randint(5, size=(5, 5))

print(matrix)

print(diagonalmatrix(matrix))
