def largest_square_submatrix(samples):
    rows = len(samples)
    cols = len(samples[0])
    
    # Create a dynamic programming table to store the sizes of largest square submatrices
    dp = [[0] * cols for _ in range(rows)]
    
    # Initialize the first row and column of the table
    for i in range(rows):
        dp[i][0] = samples[i][0]
    
    for j in range(cols):
        dp[0][j] = samples[0][j]
   
    
    # Fill the remaining cells of the table
    for i in range(1, rows):
        for j in range(1, cols):
            if samples[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    # Find the maximum value in the table
    max_size = max(max(row) for row in dp)
    
    return max_size

# Test the function with the given samples
samples = [[1,1,1,1], [1,1,1, 0], [1,1,1,1], [0,0,0,0]]
result = largest_square_submatrix(samples)
print(result)  # Output: 3