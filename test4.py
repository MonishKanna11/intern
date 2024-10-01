
SIZE = 5

def is_valid(grid, row, col, num):
    for i in range(SIZE):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    return True 
def solve_sudoku(grid):
    
    for row in range(SIZE):
        for col in range(SIZE):
            if grid[row][col] == 0:
            
                for num in range(1, SIZE + 1):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num

                        
                        if solve_sudoku(grid):
                            return True

                        
                        grid[row][col] = 0

                return False

    return True

def print_sudoku(grid):
    for row in grid:
        print(row)

puzzle = [
    [1, 0, 0, 0, 0],
    [0, 0, 0, 3, 0],
    [0, 0, 3, 0, 0],
    [0, 4, 0, 0, 0],
    [0, 0, 0, 0, 5]
]


if solve_sudoku(puzzle):
    print("Solved Sudoku Grid:")
    print_sudoku(puzzle)
else:
    print("No solution exists.")

