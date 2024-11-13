import numpy as np
import sys
import termcolor

global singles_list
singles_list = []
global singles_inserted
singles_inserted = 0


def print_sudoku(sudoku,num_rows,num_cols):
    global singles_list
    for i in range(num_rows):
        for j in range(num_cols):
            if any([i, j] in sublist for sublist in singles_list):
                termcolor.cprint(sudoku[i,j],'blue','on_green',end = ' ')
            else:
                print(sudoku[i,j], end=" ")
        print("\n")
    return

def find_singles(sudoku,num_rows,num_cols):
    global singles_list
    global singles_inserted
    pos_list = []
    for i in range(0,num_rows,3):
        for j in range(0,num_cols,3):
            for k in range(10):
                if check_subgrid(sudoku,i,j,k):
                    pos_list = iter_subgrid(sudoku,i,j,k)
                    if len(pos_list) == 1:
                        sudoku[pos_list[0][0],pos_list[0][1]] = k
                        singles_inserted+=1
                        singles_list.append(pos_list)
                        find_singles(sudoku,num_rows,num_cols)
                    else:
                        pos_list.clear()
    return
def iter_subgrid(sudoku,x,y,k):
    count = 0
    pos_list = []
    row_idx = (x//3)*3
    col_idx = (y//3)*3
    # print("checking for {} in subgrid {}{}".format(k,row_idx,col_idx))
    for i in range(row_idx,row_idx+3):
        for j in range(col_idx,col_idx+3):
            if sudoku[i,j]==0:
                if check_rows(sudoku,num_rows,i,j,k) and check_cols(sudoku,num_cols,i,j,k):
                    count = count + 1
                    pos_list.append([i,j])
    # print("{}can be inserted at {}positions within this subgrid".format(k,count))
    if count == 1:
        return pos_list
    else:
        pos_list.clear()
        return pos_list 


def naive_backtrack(sudoku,num_rows,num_cols,x,y):
    k = 1
    if x< num_rows:
        if sudoku[x,y] == 0:
            while k<10:
                if check_rows(sudoku,num_rows,x,y,k) and check_cols(sudoku,num_cols,x,y,k) and check_subgrid(sudoku,x,y,k):
                    sudoku[x,y] = k 
                    naive_backtrack(sudoku,num_rows,num_cols,x+1,y)
                    k+=1
                else:
                    k+=1
                
            sudoku[x,y] = 0
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
    for i in range(num_rows):
        if i!=x and sudoku[i,y] == k:
            return False
    return True

def check_cols(sudoku,num_cols,x,y,k):
    for j in range(num_cols):
        if j!=y and sudoku[x,j] == k:
            return False
    return True

def check_subgrid(sudoku,x,y,k):
    row_start = int(x/3)*3
    col_start = int(y/3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[row_start+i][col_start+j]==k:
                return False
    return True

sudoku = np.array([[0,0,0,0,0,0,2,0,0],
                   [0,8,0,0,0,7,0,9,0],
                   [6,0,2,0,0,0,5,0,0],
                   [0,7,0,0,6,0,0,0,0],
                   [0,0,0,9,0,1,0,0,0],
                   [0,0,0,0,2,0,0,4,0],
                   [0,0,5,0,0,0,6,0,3],
                   [0,9,0,4,0,0,0,7,0],
                   [0,0,6,0,0,0,0,0,0],
                   ])
num_rows = sudoku.shape[0]
num_cols = sudoku.shape[1]
x = 0
y = 0
print("INITIAL BOARD: ")
print_sudoku(sudoku,num_rows,num_cols)
find_singles(sudoku,num_rows,num_cols)
print("{} SINGLES FILLED BOARD: ".format(singles_inserted))
print_sudoku(sudoku,num_rows,num_cols)
naive_backtrack(sudoku,num_rows,num_cols,x,y)