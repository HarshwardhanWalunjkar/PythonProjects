import numpy as np

def print_sudoku(sudoku,num_rows,num_cols):
    for i in range(num_rows):
        for j in range(num_cols):
            print(sudoku[i,j], end=" ")
        print("\n")
    return

def find_singles(sudoku,num_rows,num_cols):
    for i in range(num_rows):
        for j in range(num_cols):
            store_k=[]
            if sudoku[i,j]==0:
                for k in range(1,10):
                    if check_rows(sudoku,num_rows,i,j,k) and check_cols(sudoku,num_cols,i,j,k) and check_subgrid(sudoku,i,j,k):
                        store_k.append(k)
                if len(store_k) == 1:
                    print("\nsingle found in cell {},{} and the number is {}".format(i,j,store_k[0]))
                    sudoku[i,j] = store_k[0]
                    store_k.clear()
                    find_singles(sudoku,num_rows,num_cols)
                else:
                    store_k.clear()
    return

# def naive_backtrack(sudoku,num_rows,num_cols,x,y):
#     k = 1
#     if x< num_rows:
#         if sudoku[x,y] == 0:
#             while k<10:
#                 if check_rows(sudoku,num_rows,x,y,k) and check_cols(sudoku,num_cols,x,y,k) and check_subgrid(sudoku,x,y,k):
#                     sudoku[x,y] = k 
#                     naive_backtrack(sudoku,num_rows,num_cols,x+1,y)
#                     k+=1
#                 else:
#                     k+=1
                
#             sudoku[x,y] = 0
#             return
#         else:
#             naive_backtrack(sudoku,num_rows,num_cols,x+1,y)
#     else:
#         if y+1<num_cols:
#             naive_backtrack(sudoku,num_rows,num_cols,0,y+1)
#         else:
#             print("\n")
#             print_sudoku(sudoku,num_rows,num_cols)
#             inp = input("More....? : ")
#             return


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
    row_start = int(x//3)*3
    col_start = int(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if i!=x and j!=y:
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
print("SINGLES FILLED BOARD: ")
print_sudoku(sudoku,num_rows,num_cols)
# print("SOLVED BOARD: ")
# naive_backtrack(sudoku,num_rows,num_cols,x,y)