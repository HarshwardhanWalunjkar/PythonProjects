import pygame
import random

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

WIDTH = 800
HEIGHT = 800
TILE_SIZE = 20
GRID_HEIGHT = HEIGHT//20
GRID_WIDTH = WIDTH//20
FPS = int(60)

#note in pygame the upper left corner is (0,0) and the y increases down and x increases to the right
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def draw_grid(positions,tumor_positions,immune_positions):
    for pos in positions:
        col, row = pos
        top_left = (col*TILE_SIZE,row*TILE_SIZE)
        pygame.draw.rect(screen,GREEN,(*top_left,TILE_SIZE,TILE_SIZE))
    for pos in tumor_positions:
        col, row = pos
        top_left = (col*TILE_SIZE,row*TILE_SIZE)
        pygame.draw.rect(screen,RED,(*top_left,TILE_SIZE,TILE_SIZE))
    for pos in immune_positions:
        col, row = pos
        top_left = (col*TILE_SIZE,row*TILE_SIZE)
        pygame.draw.rect(screen,BLUE,(*top_left,TILE_SIZE,TILE_SIZE))    
    for row in range(GRID_WIDTH):
        pygame.draw.line(screen,WHITE,(0,row*TILE_SIZE),(WIDTH,row*TILE_SIZE))
    for col in range(GRID_HEIGHT):
        pygame.draw.line(screen,WHITE,(col*TILE_SIZE,0),(col*TILE_SIZE,HEIGHT))

def evolve_life(positions,tumor_positions, immune_positions):
    all_neighbors = set()
    new_positions = set()
    tumor_neighbors = set()
    new_tumors = set()
    new_tumors.update(tumor_positions)
    new_immune = set()
    new_immune.update(immune_positions)
    for position in positions:
        #gets nieghbors of the live cell
        neighbors = get_neighbors(position)
        #form a set of all neighbors of all live cells which are not tumor cells
        for neighbor in neighbors:
            if neighbor not in new_tumors and neighbor not in new_immune:
                all_neighbors.update (neighbors)
        #consider only live and dead cell neibors of the all the cells to give all neighbors
        #filter neighbors of each live cell position to get only live cell neighbors
        neighbors = list(filter(lambda x: x in positions and x not in new_tumors and x not in new_immune, neighbors))
        if len(neighbors) == 1 or len(neighbors) == 2 or len(neighbors) == 3:
            new_positions.add(position)
    
    #check for reproduction in conway by considering only relevant cells which are all neighbors
    #all_neighbors already do not include immune or tumor cells
    for position in all_neighbors:
        neighbors = get_neighbors(position)
    #find how many live nighbors each relevant cell has and decide reproduction accordingly
        neighbors = list(filter(lambda x: x in positions,neighbors))
        if len(neighbors) == 3:
            new_positions.add(position)
    #any dead cell with more than 4 live neighbors becomes immune by nutritional power
        if len(neighbors)==8:
            new_immune.add(position)


    for tumor in tumor_positions:
        tumor_neighbors = get_neighbors(tumor)
        for neighbor in tumor_neighbors:
            if neighbor in new_positions:
                new_positions.remove(neighbor)
                new_tumors.add(neighbor)
            # if neighbor in immune_positions:
            #     #new_tumors.remove(tumor)
            #     new_immune.add(neighbor)
    for immune_cell in immune_positions:
        immune_neighbors = get_neighbors(immune_cell)
        kill_protein = list(filter(lambda x: x in new_tumors,immune_neighbors))
        if len(kill_protein)>=4:
            new_immune.remove(immune_cell)
            new_tumors.add(immune_cell)
        else:
            for neighbor in immune_neighbors:
                if neighbor in new_tumors:
                    new_tumors.remove(neighbor)
                    rand = random.randint(1,10)
                    if rand >=5:
                        new_immune.add(neighbor)
                    else:
                        new_positions.add(neighbor)
    return new_positions,new_tumors,new_immune

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
    playing = False
    positions = set()
    tumor_positions = set()
    immune_positions = set()
    tumor = (10,10)
    tumor_positions.add(tumor)
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
            positions,tumor_positions,immune_positions = evolve_life(positions,tumor_positions,immune_positions)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_pressed()[0]:
                x,y = pygame.mouse.get_pos()
                col = x//TILE_SIZE
                row = y//TILE_SIZE
                pos = (col,row)
                if pos in positions:
                    positions.remove(pos)
                elif pos in tumor_positions:
                    tumor_positions.remove(pos)
                else:
                    positions.add(pos)
                
            if pygame.mouse.get_pressed()[2]:
                x,y = pygame.mouse.get_pos()
                col = x//TILE_SIZE
                row = y//TILE_SIZE
                pos = (col,row)
                if pos in tumor_positions:
                    tumor_positions.remove(pos)
                elif pos in positions:
                    positions.remove(pos)
                else:
                    tumor_positions.add(pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                if event.key == pygame.K_r:
                    positions = set()
                    tumor_positions = set()
                    immune_positions = set()
                    playing = False
                    count = 0
                if event.key == pygame.K_g:
                    for _ in range(random.randint(4,8)*GRID_HEIGHT):
                        pos = (random.randint(0,GRID_WIDTH),random.randint(0,GRID_HEIGHT))
                        positions.add(pos)

        screen.fill(BLACK)
        draw_grid(positions,tumor_positions,immune_positions)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()