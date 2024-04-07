import numpy as np

def max_pooling(matrix, window_size):
    row = len(matrix)
    column = len(matrix[0])
    k = window_size

    # Output matrix to store maximum values
    output = np.zeros((row - k + 1, column - k + 1))

    # Initialize dynamic programming table
    dp = np.zeros((row, column))
    dp[:k, :] = matrix[:k, :]
    dp[:, :k] = matrix[:, :k]

    # Compute dynamic programming table
    for i in range(1, row):
        for j in range(1, column):
            dp[i, j] = max(dp[i-1, j], dp[i, j-1], matrix[i, j])

    # Compute output matrix using dynamic programming table
    for i in range(row - k + 1):
        for j in range(column - k + 1):
            output[i, j] = dp[i+k-1, j+k-1]

    return output

# Example usage
# Considering m x m matrix
row=int(input("Enter Number of Rows: "))
column=int(input("Enter Number of Columns: "))
mat=[[0 for _ in range(column)] for _ in range(row)]
for i in range(row):
    for j in range(column):
        mat[i][j]=int(input(f"Enter vatue for mat[{i}][{j}] = "))
print(mat)
matrix = np.array(mat)

window_size = int(input("Enter Winddow Size: "))
result = max_pooling(matrix, window_size)

print("Resut Matrix")
print(result)
