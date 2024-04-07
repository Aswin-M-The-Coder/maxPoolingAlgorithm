import numpy as np

def max_pooling(matrix, window_size):
    row = len(matrix)
    column = len(matrix[0])
    k = window_size

    # Output matrix to store maximum values
    output = np.zeros((row - k + 1, column - k + 1))

    # Iterate through each position of the moving window
    for i in range(row - k + 1):
        for j in range(column - k + 1):
            # Extract the window
            window = matrix[i:i+k, j:j+k]
            # Calculate the maximum value in the window
            max_value = np.max(window)
            # Assign the maximum value to the corresponding position in the output matrix
            output[i, j] = max_value

    return output

# Example usage
# Considering m x n matrix
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
