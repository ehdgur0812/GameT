import pygame
import time
import Tile
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
x_speed = 20
y_speed = 20
        
pygame.init()
screen = pygame.display.set_mode([400, 600])
pygame.display.set_caption('CMSC 150 is cool')
clock = pygame.time.Clock()
background_position = [0, 0]

background_image = pygame.image.load("GameBG.png").convert()


tiles = list()
for y_index in range(30) :
    tiles.append(list())
    for x_index in range(20) :
        tiles[y_index].append(Tile.TileClass())
        tiles[y_index][x_index].initTile(y_index, x_index, pygame)

now_time = time.time()
down_time = time.time() + 0.5

done = False

Tile.randomTile(tiles)

reSetState = False

bol = True
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                Tile.leftMove(tiles, 30, 20)
            if event.key == pygame.K_RIGHT :
                Tile.rightMove(tiles, 30, 20)
            if event.key == pygame.K_SPACE :
                Tile.speedMove(tiles, 30, 20)
                Tile.randomTile(tiles)
            if event.key == pygame.K_ESCAPE :
                bol = False

    now_time = time.time()
    if(now_time >= down_time) :
        if bol == True :
            reSetState = Tile.downTile(tiles, 30, 20)
        down_time = now_time + 0.5
        
    if reSetState == True :
        Tile.randomTile(tiles)
        reSetState = False
 
    screen.blit(background_image, background_position)

    for y_index in range(30) :
        for x_index in range(20) :
            if(tiles[y_index][x_index].block == 1) :
                screen.blit(tiles[y_index][x_index].image,
                            [tiles[y_index][x_index].x_position, tiles[y_index][x_index].y_position])
 
 
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
