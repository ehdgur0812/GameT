import pygame
import time
import Tile
import TileRotation
import TileCheck
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
x_speed = 20
y_speed = 20

x_line = 50
y_line = 30
        
pygame.init()
screen = pygame.display.set_mode([1100, 600])
pygame.display.set_caption('CMSC 150 is cool')
clock = pygame.time.Clock()
background_position = [0, 0]

background_image = pygame.image.load("DarkBG.png").convert()
block_general_image = pygame.image.load("block\general.png").convert()
block_general_image.set_colorkey((0,0,0))
block_add_image = pygame.image.load("block\genadd.png").convert()
block_add_image.set_colorkey((0,0,0))

tiles = list()
for y_index in range(y_line) :
    tiles.append(list())
    for x_index in range(x_line) :
        tiles[y_index].append(Tile.TileClass())
        tiles[y_index][x_index].initTile(y_index, x_index, pygame)

now_time = time.time()
down_time = time.time() + 0.5

done = False

rotation_type = Tile.randomTile(tiles)

reSetState = False

bol = True
rotation_index = 0
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                Tile.leftMove(tiles, y_line, x_line)
            elif event.key == pygame.K_RIGHT :
                Tile.rightMove(tiles, y_line, x_line)
            elif event.key == pygame.K_SPACE :
                Tile.speedMove(tiles, y_line, x_line)
                #rotation_type = Tile.randomTile(tiles)
                #rotation_index = 0
                reSetState = True
            elif event.key == pygame.K_UP :
                rotation_index = TileRotation.RotateTile(tiles, y_line, x_line, rotation_type, rotation_index)
            elif event.key == pygame.K_ESCAPE :
                bol = False

    TileCheck.CheckTile(tiles, y_line, x_line)

    now_time = time.time()
    if now_time >= down_time :
        if bol == True and reSetState != True:
            #reSetState = False
            reSetState = Tile.downTile(tiles, y_line, x_line)
        down_time = now_time + 0.5
        
    if reSetState == True :
        rotation_type = Tile.randomTile(tiles)
        reSetState = False
        rotation_index = 0

    Tile.ghostMove(tiles, y_line, x_line)
 
    screen.blit(background_image, background_position)

    for y_index in range(y_line) :
        for x_index in range(x_line) :
            if tiles[y_index][x_index].block == 1 :
                screen.blit(block_general_image,
                            [tiles[y_index][x_index].x_position+100, tiles[y_index][x_index].y_position])
            elif tiles[y_index][x_index].block == 2 :
                 screen.blit(block_add_image,
                            [tiles[y_index][x_index].x_position+100, tiles[y_index][x_index].y_position])
 
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
