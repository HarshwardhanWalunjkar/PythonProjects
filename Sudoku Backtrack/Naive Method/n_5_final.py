import numpy as np

def print_sudoku(sudoku,num_rows,num_cols):
    for i in range(num_rows):
        for j in range(num_cols):
            print(sudoku[i,j], end=" ")
        print("\n")

def naive_backtrack(sudoku,num_rows,num_cols,x,y):
    k = 1
    if x< num_rows:
        if sudoku[x,y] == -1:
            while k<10:
                if check_rows(sudoku,num_rows,x,y,k) and check_cols(sudoku,num_cols,x,y,k) and check_subgrid(sudoku,x,y,k):
                    sudoku[x,y] = k 
                    naive_backtrack(sudoku,num_rows,num_cols,x+1,y)
                    k+=1
                else:
                    k+=1
                
            sudoku[x,y] = -1
            return
        else:
            naive_backtrack(sudoku,num_rows,num_cols,x+1,y)
    else:
        if y+1<num_cols:
            naive_backtrack(sudoku,num_rows,num_cols,0,y+1)
        else:
            print("\n")
            print_sudoku(sudoku,num_rows,num_cols)
            inp = input("More....? : ")
            return




def check_rows(sudoku,num_rows,x,y,k):
  #  print("checking rows at {},{} for value {}".format(x,y,k))
    for i in range(num_rows):
        if i!=x and sudoku[i,y] == k:
          #  print("{} cannot be used at {},{}".format(k,x,y))
            return 0
  #  print("{} can be used at {},{}".format(k,x,y))
    return 1

def check_cols(sudoku,num_cols,x,y,k):
   # print("checking cols at {},{} for value {}".format(x,y,k))
    for j in range(num_cols):
        if j!=y and sudoku[x,j] == k:
           # print("{} cannot be used at {},{}".format(k,x,y))
            return 0
    #print("{} can be used at {},{}".format(k,x,y))
    return 1

def check_subgrid(sudoku,x,y,k):
    row_start = int(x/3)*3
    col_start = int(y/3)*3
    for i in range(0,3):
        for j in range(0,3):
            if i!=x and j!=y:
                if sudoku[row_start+i][col_start+j]==k:
                    return 0
    return 1

    
sudoku = np.array([[-1,-1,-1,-1,-1,-1,2,-1,-1],
                   [-1,8,-1,-1,-1,7,-1,9,-1],
                   [6,-1,2,-1,-1,-1,5,-1,-1],
                   [-1,7,-1,-1,6,-1,-1,-1,-1],
                   [-1,-1,-1,9,-1,1,-1,-1,-1],
                   [-1,-1,-1,-1,2,-1,-1,4,-1],
                   [-1,-1,5,-1,-1,-1,6,-1,3],
                   [-1,9,-1,4,-1,-1,-1,7,-1],
                   [-1,-1,6,-1,-1,-1,-1,-1,-1],
                   ])


num_rows = sudoku.shape[0]
num_cols = sudoku.shape[1]
x = 0
y = 0
print_sudoku(sudoku,num_rows,num_cols)
naive_backtrack(sudoku,num_rows,num_cols,x,y)