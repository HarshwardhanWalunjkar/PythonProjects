import pygame
import random

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

WIDTH = 800
HEIGHT = 800
TILE_SIZE = 20
GRID_HEIGHT = HEIGHT//20
GRID_WIDTH = WIDTH//20
FPS = int(60)

#note in pygame the upper left corner is (0,0) and the y increases down and x increases to the right
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def draw_grid(positions):
    for pos in positions:
        col, row = pos
        top_left = (col*TILE_SIZE,row*TILE_SIZE)
        pygame.draw.rect(screen,GREEN,(*top_left,TILE_SIZE,TILE_SIZE))
    for row in range(GRID_WIDTH):
        pygame.draw.line(screen,WHITE,(0,row*TILE_SIZE),(WIDTH,row*TILE_SIZE))
    for col in range(GRID_HEIGHT):
        pygame.draw.line(screen,WHITE,(col*TILE_SIZE,0),(col*TILE_SIZE,HEIGHT))

def adjust_grid(positions):
    all_neighbors = set()
    new_positions = set()

    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update (neighbors)
        neighbors = list(filter(lambda x: x in positions, neighbors))
        if len(neighbors) == 2 or len(neighbors) == 3:
            new_positions.add(position)
    
    for position in all_neighbors:
        neighbors = get_neighbors(position)
        neighbors = list(filter(lambda x: x in positions,neighbors))
        if len(neighbors) == 3:
            new_positions.add(position)

    return new_positions


def get_neighbors(pos):
    x,y = pos
    neighbors = []
    for dx in [-1, 0, 1]:
        if (x+dx)<0 or (x+dx)>GRID_WIDTH:
            continue
        for dy in [-1 , 0 , 1]:
            if (y+dy)<0 or (y+dy)>GRID_HEIGHT:
                continue
            if dx == 0 and dy == 0:
                continue
            neighbors.append((x+dx,y+dy))
    return neighbors

def main():
    running = True
    playing = True
    positions = set()
    count = 0
    update_freq = 6

    while running == True:
        clock.tick(FPS)

        if playing:
            count+=1
            pygame.display.set_caption("PLAYING")
        else: 
            pygame.display.set_caption("NOT PLAYING/PAUSED")
        
        if count>=update_freq:
            count = 0
            positions = adjust_grid(positions)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                col = x//TILE_SIZE
                row = y//TILE_SIZE
                pos = (col,row)
                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                if event.key == pygame.K_r:
                    positions = set()
                    playing = False
                    count = 0
                if event.key == pygame.K_g:
                    for _ in range(random.randint(4,8)*GRID_HEIGHT):
                        pos = (random.randint(0,GRID_WIDTH),random.randint(0,GRID_HEIGHT))
                        positions.add(pos)

        screen.fill(BLACK)
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()