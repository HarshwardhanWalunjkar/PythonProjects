import numpy as np

def print_sudoku(sudoku, num_rows, num_cols):
    for i in range(num_rows):
        for j in range(num_cols):
            print(sudoku[i, j], end=" ")
        print()
    print()  # Add a newline for better readability

def naive_backtrack(sudoku, num_rows, num_cols, x, y):
    if x == num_rows:
        if y + 1 == num_cols:
            print("\nSolved Sudoku:\n")
            print_sudoku(sudoku, num_rows, num_cols)
            inp = input("More....? (yes/no): ").strip().lower()
            if inp == "yes":
                return False  # Continue solving
            else:
                exit()  # Exit the program
        else:
            return naive_backtrack(sudoku, num_rows, num_cols, 0, y + 1)

    if sudoku[x, y] == -1:
        for k in range(1, 10):
            if check_rows(sudoku, num_rows, x, y, k) and check_cols(sudoku, num_cols, x, y, k) and check_subgrid(sudoku, x, y, k):
                sudoku[x, y] = k
                if naive_backtrack(sudoku, num_rows, num_cols, x + 1, y):
                    return True
                sudoku[x, y] = -1
        return False
    else:
        return naive_backtrack(sudoku, num_rows, num_cols, x + 1, y)

def check_rows(sudoku, num_rows, x, y, k):
    for i in range(num_rows):
        if sudoku[i, y] == k:
            return False
    return True

def check_cols(sudoku, num_cols, x, y, k):
    for j in range(num_cols):
        if sudoku[x, j] == k:
            return False
    return True

def check_subgrid(sudoku, x, y, k):
    row_start = (x // 3) * 3
    col_start = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[row_start + i, col_start + j] == k:
                return False
    return True

sudoku = np.array([[-1, -1, -1, -1, -1, -1, 2, -1, -1],
                   [-1, 8, -1, -1, -1, 7, -1, 9, -1],
                   [6, -1, 2, -1, -1, -1, 5, -1, -1],
                   [-1, 7, -1, -1, 6, -1, -1, -1, -1],
                   [-1, -1, -1, 9, -1, 1, -1, -1, -1],
                   [-1, -1, -1, -1, 2, -1, -1, 4, -1],
                   [-1, -1, 5, -1, -1, -1, 6, -1, 3],
                   [-1, 9, -1, 4, -1, -1, -1, 7, -1],
                   [-1, -1, 6, -1, -1, -1, -1, -1, -1]])

num_rows = sudoku.shape[0]
num_cols = sudoku.shape[1]
x = 0
y = 0

print("Initial Sudoku:")
print_sudoku(sudoku, num_rows, num_cols)
while naive_backtrack(sudoku, num_rows, num_cols, x, y) == False:
    continue

