import Tile

def ChangeTile(tiles, y_index, x_index, y_change, x_change) :
    tiles[y_index][x_index].block = tiles[y_change][x_change].block
    tiles[y_index][x_index].hold = tiles[y_change][x_change].hold
    tiles[y_change][x_change].reInit()

def CheckTile(tiles, y_size, x_size) :
    y_offset = y_size - 1
    correct_state = True
    for y_index in range(y_size) :
        correct_state = True
        for x_index in range(x_size) :
            if tiles[y_offset][x_index].block != 1 or tiles[y_offset][x_index].hold != True :
                correct_state = False
        if correct_state == True :
            RemoveTile(tiles, y_size, x_size, y_offset)
            y_offset -= 1
        y_offset -= 1

def RemoveTile(tiles, y_size, x_size, y_offset) :
    y_line = 0
    for y_index in range(y_offset-1) :
        y_line = y_offset - y_index
        for x_index in range(x_size) :
            tiles[y_line][x_index].reInit()
            ChangeTile(tiles, y_line, x_index, y_line-1, x_index)
                
