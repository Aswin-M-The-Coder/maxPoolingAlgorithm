Max Pooling Problem

Prerequisite:
		VS code / Python Compiler

Procedure:
	Step 1: Open vs code terminal and clone the below git repository
https://github.com/Aswin-M-The-Coder/maxPoolingAlgorithm.git
	Step 2: Run the python files
Comparison:

i) Normal / Usual Algorithm(maxPooling.py)

Time Complexity:
Worst-case time complexity: O(m^2 * k^2)
This occurs when we have to iterate through every position of the moving window for each position of the input matrix. In the worst case, the algorithm has to visit every element of the input matrix, and for each element, it has to iterate through a window of size k^2 to find the maximum value.
Best-case time complexity: O(m^2)
The best case occurs when the window size is 1x1, meaning we don't need to iterate through a window, and we can simply assign the input matrix elements to the output matrix. In this case, the time complexity is proportional to the size of the input matrix, which is m^2. However, note that this best-case scenario is rarely encountered in practical applications, as typically the window size will be larger than 1x1.
	
 ii) Optimized Solution Using DP (optimizedMaxPooling.py)

Time Complexity:
Worst-case time complexity: O(m^2)
The worst-case time complexity occurs when the input matrix is large and we have to compute the dynamic programming table for every element of the matrix, which takes O(m^2) time.
Best-case time complexity: O(m^2)
The best-case time complexity also occurs when we have to compute the dynamic programming table for every element of the matrix, which takes O(n^2) time.
