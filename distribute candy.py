def candy(A):
    n = len(A)
    candies = [1] * n  # Initialize with 1 candy for each child

    # First pass: From left to right
    for i in range(1, n):
        if A[i] > A[i-1]:
            candies[i] = candies[i-1] + 1

    # Second pass: From right to left
    for i in range(n-2, -1, -1):
        if A[i] > A[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    # Calculate the total number of candies
    total_candies = sum(candies)
    
    return total_candies

# Example
A = [1, 2]
result = candy(A)
print(result)  # Output: 3
