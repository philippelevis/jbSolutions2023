from tabulate import tabulate


n = 25
matrix = [["" for _ in range(n)] for _ in range(n)]  # Initialize matrix with empty strings

for i in range(n):
    j = i+1
    matrix[i][i] = j * j - j + 1  # Fill main diagonal with formula n^2 - n + 1
    row, col = i, i
    
    # Fill cells above the main diagonal with "a"
    while row > 0:
        row -= 1
        if i%2 == 0:
            matrix[row][col] = matrix[row+1][col]+1
        else:
            matrix[row][col] = matrix[row+1][col]-1
        
    
    # Fill cells to the left of the main diagonal with "b"
    row, col = i, i
    while col > 0:
        col -= 1
        if i%2 == 0:
            matrix[row][col] = matrix[row][col+1]-1
        else:
            matrix[row][col] = matrix[row][col+1]+1

# Print the filled matrix
table = tabulate(matrix, tablefmt="grid")
print(table)
