import Tile

_pygame = 0
boom_sound = 0

def set_Sound(pygame) :
    global boom_sound, _pygame
    _pygame = pygame
    boom_sound = _pygame.mixer.Sound('sound/explosion.wav')

def ChangeTile(tiles, y_index, x_index, y_change, x_change) :
    global boom_sound, _pygame
    tiles[y_index][x_index].block = tiles[y_change][x_change].block
    tiles[y_index][x_index].hold = tiles[y_change][x_change].hold
    tiles[y_change][x_change].reInit()
    _pygame.mixer.Sound.play(boom_sound)

def CheckTile(tiles, y_size, x_size) :
    y_offset = y_size - 1
    correct_state = True
    while y_offset >= 0 :
        correct_state = True
        for x_index in range(x_size) :
            if tiles[y_offset][x_index].block != 1 or tiles[y_offset][x_index].hold != True :
                correct_state = False
        if correct_state == True :
            RemoveTile(tiles, y_size, 0, x_size-1, y_offset, 0)
            y_offset += 1
        y_offset -= 1

def FindUpBlockType5(tiles, y_offset, x_offset) :
    while y_offset >= 0 :
        if tiles[y_offset][x_offset].block != 5 :
            break;
        y_offset-=1
    return y_offset+1

def CheckTileType5(tiles, y_size, x_size) :
    y_offset = y_size - 1
    correct_state = False
    x_start = 0
    x_end = 0
    while y_offset >= 0 :
        correct_state = False
        x_start = 0
        x_end = 0
        for x_index in range(x_size) :
            if tiles[y_offset][x_index].block == 5 and correct_state == False :
                x_start = x_index
                correct_state = True
            elif tiles[y_offset][x_index].block == 5 and correct_state == True :
                x_end = x_index
                RemoveTile(tiles, y_size, x_start, x_end, y_offset,
                           FindUpBlockType5(tiles, y_offset, x_start))
                y_offset += 1
                break
            elif correct_state == True :
                if tiles[y_offset][x_index].block != 1 or tiles[y_offset][x_index].hold != True :
                    correct_state = False
                    break
        y_offset -= 1

def RemoveTile(tiles, y_size, x_start, x_end, y_offset, y_end) :
    global boom_sound, _pygame
    y_line = 0
    x_index = x_start
    if y_offset == y_end :
        while x_index <= x_end :
            tiles[y_offset][x_index].reInit()
            x_index+=1
            _pygame.mixer.Sound.play(boom_sound)
    if y_offset != y_end :
        for y_index in range(y_offset) :
            y_line = y_offset - y_index
            if y_line == y_end :
                break;
            x_index = x_start
            while x_index <= x_end :
                tiles[y_line][x_index].reInit()
                ChangeTile(tiles, y_line, x_index, y_line-1, x_index)
                x_index+=1
                
