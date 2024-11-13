import pygame
import numpy as np

global singles_list
singles_list = []
global singles_inserted
singles_inserted = 0

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WIDTH = 450
HEIGHT = 450
BOX_SIZE = 50
ROWS = HEIGHT//BOX_SIZE
COLS = WIDTH//BOX_SIZE
FONT_SIZE = BOX_SIZE//2
screen = pygame.display.set_mode((WIDTH,HEIGHT))
font = pygame.font.SysFont(None, FONT_SIZE)


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
#find_singles(sudoku,num_rows,num_cols)
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
                        found(pos_list[0][0],pos_list[0][1])
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
                accessed(i,j)
                if check_rows(sudoku,num_rows,i,j,k) and check_cols(sudoku,num_cols,i,j,k):
                    count = count + 1
                    pos_list.append([i,j])
    # print("{}can be inserted at {}positions within this subgrid".format(k,count))
    if count == 1:
        return pos_list
    else:
        pos_list.clear()
        return pos_list 
    

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

def make_grid():
    for i in range(ROWS+1):
        if i%3 == 0 and i != 0 and i!= 9:
            pygame.draw.line(screen,BLACK,(0,i*BOX_SIZE),(WIDTH,i*BOX_SIZE),width=5)
        else:
            pygame.draw.line(screen,BLACK,(0,i*BOX_SIZE),(WIDTH,i*BOX_SIZE),width=1)
    for j in range(COLS+1):
        if j%3 == 0 and j != 0 and j!= 9:
            pygame.draw.line(screen,BLACK,(j*BOX_SIZE,0),(j*BOX_SIZE,HEIGHT),width=5)
        else:
            pygame.draw.line(screen,BLACK,(j*BOX_SIZE,0),(j*BOX_SIZE,HEIGHT),width=1)
    for i in range(sudoku.shape[0]):
        for j in range(sudoku.shape[1]):
            if sudoku[i,j]!=0:
                text = font.render(str(sudoku[i,j]),True,BLACK)
                text_rect = text.get_rect(center = (j*BOX_SIZE + BOX_SIZE//2,i*BOX_SIZE + BOX_SIZE//2))
                screen.blit(text,text_rect)

def accessed(ROW,COL):
    rect = pygame.Rect(COL*BOX_SIZE,ROW*BOX_SIZE,BOX_SIZE,BOX_SIZE)
    pygame.draw.rect(screen,BLUE,rect,width=5)
    pygame.display.update()

def found(ROW,COL):
    rect = pygame.Rect(COL*BOX_SIZE,ROW*BOX_SIZE,BOX_SIZE,BOX_SIZE)
    pygame.draw.rect(screen,GREEN,rect,width=10)
    pygame.display.update()

def wrong(ROW,COL):
    rect = pygame.Rect(COL*BOX_SIZE,ROW*BOX_SIZE,BOX_SIZE,BOX_SIZE)
    pygame.draw.rect(screen,RED,rect,width=10)
    pygame.display.update()

def main():
    running = True
    x = 0
    y = 0
    while running:
        screen.fill(WHITE)
        make_grid()
        pygame.display.update()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    find_singles(sudoku,num_rows,num_cols)
if __name__ == "__main__":
    main()