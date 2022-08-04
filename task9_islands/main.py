import numpy as np


def dfs(matrix, i, j):
    if i < 0 or j < 0 or i >= matrix.shape[0] or j >= matrix.shape[1] or matrix[i][j] == '0':
        return
    matrix[i][j] = '0'
    dfs(matrix, i - 1, j)
    dfs(matrix, i + 1, j)
    dfs(matrix, i, j - 1)
    dfs(matrix, i, j + 1)


def num_islands(matrix):
    rows, cols = matrix.shape
    if rows == 0:
        return 0
    count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                count += 1
                dfs(matrix, i, j)
    return count


a = np.array([['1', '1', '0', '0', '0'],
              ['1', '1', '0', '0', '0'],
              ['0', '0', '1', '0', '0'],
              ['0', '0', '0', '1', '0']])

print(num_islands(a))
