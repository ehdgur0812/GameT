import Tile
import TileRotation
import TileCheck
import time

rotation_type = 0
rotation_index = 0
reSetState = False
allHoldState = False
allHoldTime = 0.0

left_move = False
right_move = False
down_move = False
left_time = 0.0
right_time = 0.0

down_sound = 0

def init_Tetris(pygame, tiles, y_line, x_line) :
    global rotation_type, rotation_index
    global reSetState, allHoldState, allHoldTime
    global left_move, right_move
    global down_sound
    
    reSetState = False
    allHoldState = False
    allHoldTime = 0.0
    for y_index in range(y_line) :
        for x_index in range(x_line) :
            tiles[y_index][x_index].reInit()
    rotation_type = Tile.randomTile(tiles)
    rotation_index = 0
    left_move = False
    right_move = False

    down_sound = pygame.mixer.Sound('sound/shot.wav')
    TileCheck.set_Sound(pygame)
    #Tile.ghostTMove(tiles, y_line, x_line)

def play_Tetris(pygame, tiles, y_line, x_line, now_time, down_time) :
    global rotation_type, rotation_index
    global reSetState, allHoldState, allHoldTime
    global left_move, right_move, down_move
    global left_time, right_time
    global down_sound

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                Tile.notNeedInit(tiles, y_line, x_line)
                return down_time, 1
            if event.key == pygame.K_LEFT :
                left_move = True
                left_time = now_time + 0.2
                Tile.leftMove(tiles, y_line, x_line)
            elif event.key == pygame.K_RIGHT :
                right_move = True
                right_time = now_time + 0.2
                Tile.rightMove(tiles, y_line, x_line)
            elif event.key == pygame.K_SPACE :
                Tile.speedMove(tiles, y_line, x_line)
                reSetState = True
            elif event.key == pygame.K_DOWN :
                down_move = True
            elif event.key == pygame.K_UP :
                rotation_index = TileRotation.RotateTile(tiles, y_line, x_line, rotation_type, rotation_index)
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT :
                left_move = False
            elif event.key == pygame.K_RIGHT :
                right_move = False
            elif event.key == pygame.K_DOWN :
                down_move = False
                
    if left_move == True and now_time >= left_time:
        Tile.leftMove(tiles, y_line, x_line)
    if right_move == True and now_time >= right_time:
        Tile.rightMove(tiles, y_line, x_line)

    TileCheck.CheckTile(tiles, y_line, x_line)
    TileCheck.CheckTileType5(tiles, y_line, x_line)

    if now_time >= down_time :
        if reSetState != True and allHoldState == False:
            reSetState = Tile.downTile(tiles, y_line, x_line)
            allHoldState = Tile.getHoldState()
            if allHoldState == True :
                allHoldTime = now_time + 0.5
        down_time = now_time + 0.5
        if down_move == True :
            down_time = now_time + 0.1
        
    if now_time >= allHoldTime and allHoldState == True :
        Tile.allHold(tiles, y_line, x_line)
        allHoldState = False
        reSetState = True
            
    if reSetState == True :
        rotation_type = Tile.randomTile(tiles)
        reSetState = False
        rotation_index = 0
        pygame.mixer.Sound.play(down_sound)

    Tile.ghostMove(tiles, y_line, x_line)

    return down_time, 0
