import numpy as np

def rec_transvere(sudoku,num_rows,num_cols,x,y):
    if x< num_rows:
        print(sudoku[x,y])
        rec_transvere(sudoku,num_rows,num_cols,x+1,y)
    else:
        if y+1<num_cols:
            return rec_transvere(sudoku,num_rows,num_cols,0,y+1)




sudoku = np.array([[1,-1,-1],[-1,3,-1],[-1,-1,1]])
num_rows = sudoku.shape[0]
num_cols = sudoku.shape[1]
x = 0
y = 0
rec_transvere(sudoku,num_rows,num_cols,x,y)