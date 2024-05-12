def transpose_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])  # Assuming all rows have the same number of elements
    
    transposed_matrix = []
    for _ in range(num_cols):
        transposed_matrix.append([0] * num_rows)
    
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = transpose_matrix(matrix)

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposed:
    print(row)
