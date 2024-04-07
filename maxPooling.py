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
matrix = np.array([[1, 3, 2, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

window_size = 2
result = max_pooling(matrix, window_size)
print(result)
