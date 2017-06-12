import Information
import Tile

x_line, y_line = Information.GetXYSize()

def ChangeTile(tiles, y_index, x_index, y_change, x_change) :
    tiles[y_index][x_index].block = tiles[y_change][x_change].block
    tiles[y_index][x_index].hold = tiles[y_change][x_change].hold
    tiles[y_change][x_change].reInit()

backTiles = list()
for y_index in range(y_line) :
    backTiles.append(list())
    for x_index in range(x_line) :
        backTiles[y_index].append(Tile.TileClass())
        
def RotateTile(tiles, y_size, x_size, rotation_type, rotation_index) :
    backRotation_index = rotation_index
    Tile.blockCopy(backTiles, tiles, y_size, x_size)
    if rotation_type == 0 :
        rotation_index = RotateType0(tiles, y_size, x_size, rotation_index)
    elif rotation_type == 1 :
        rotation_index = RotateType1(tiles, y_size, x_size, rotation_index)
    elif rotation_type == 2 :
        rotation_index = RotateType2(tiles, y_size, x_size, rotation_index)
    elif rotation_type == 3 :
        rotation_index = RotateType3(tiles, y_size, x_size, rotation_index)
    elif rotation_type == 4 :
        rotation_index = RotateType4(tiles, y_size, x_size, rotation_index)
    elif rotation_type == 5 :
        rotation_index = RotateType5(tiles, y_size, x_size, rotation_index)
        
    if Tile.getBlockSize(backTiles, y_size, x_size) != Tile.getBlockSize(tiles, y_size, x_size) :
        Tile.blockCopy(tiles, backTiles, y_size, x_size)
        rotation_index = backRotation_index
    return rotation_index

def FindOffset(tiles, y_size, x_size) :
    for y_index in range(y_size) :
        for x_index in range(x_size) :
            if tiles[y_index][x_index].block == 1 and tiles[y_index][x_index].hold == False :
                y_offset = y_index
                x_offset = x_index
                return y_offset, x_offset

def RotateType0(tiles, y_size, x_size, rotation_index) :
    y_offset, x_offset = FindOffset(tiles, y_size, x_size)
    if rotation_index == 0 :
        if x_offset == 0 :
            Tile.rightMove(tiles, y_size, x_size)
            x_offset += 1
        if x_offset >= (x_size - 2) :
            for i in range(x_offset - (x_size-2) + 1) :
                Tile.leftMove(tiles, y_size, x_size)
                x_offset -= 1
        y_offset += 1
        ChangeTile(tiles, y_offset, x_offset-1, y_offset-1, x_offset)
        ChangeTile(tiles, y_offset, x_offset+1, y_offset+1, x_offset)
        ChangeTile(tiles, y_offset, x_offset+2, y_offset+2, x_offset)
    if rotation_index == 1 :
        x_offset += 1
        if y_offset >= (y_size - 2) :
            for i in range(y_offset - (y_size-2) + 1) :
                Tile.upMove(tiles, y_size, x_size)
                y_offset -= 1
        ChangeTile(tiles, y_offset-1, x_offset, y_offset, x_offset-1)
        ChangeTile(tiles, y_offset+1, x_offset, y_offset, x_offset+1)
        ChangeTile(tiles, y_offset+2, x_offset, y_offset, x_offset+2)
    if rotation_index == 0 :
        rotation_index = 1
    elif rotation_index == 1 :
        rotation_index = 0
    return rotation_index

def RotateType1(tiles, y_size, x_size, rotation_index) :
    y_offset, x_offset = FindOffset(tiles, y_size, x_size)
    if rotation_index == 0 :
        x_offset -= 1
        if y_offset == 0 :
            Tile.downTile(tiles, y_size, x_size)
            y_offset += 1
        ChangeTile(tiles, y_offset, x_offset-1, y_offset+1, x_offset+1)
        ChangeTile(tiles, y_offset-1, x_offset-1, y_offset, x_offset+1)
    if rotation_index == 1 :
        x_offset += 1
        y_offset += 1
        if x_offset == (x_size - 1) :
            Tile.leftMove(tiles, y_size, x_size)
            x_offset -= 1
        ChangeTile(tiles, y_offset-1, x_offset, y_offset+1, x_offset)
        ChangeTile(tiles, y_offset-1, x_offset+1, y_offset+1, x_offset-1)
    if rotation_index == 2 :
        x_offset += 1
        y_offset += 1
        if y_offset == (y_size - 2) :
            Tile.upMove(tiles, y_size, x_size)
            y_offset -= 1
        ChangeTile(tiles, y_offset, x_offset+1, y_offset-1, x_offset-1)
        ChangeTile(tiles, y_offset+1, x_offset+1, y_offset, x_offset-1)
    if rotation_index == 3 :
        y_offset += 1
        if x_offset == 0 :
            Tile.rightMove(tiles, y_size, x_size)
            x_offset += 1
        ChangeTile(tiles, y_offset+1, x_offset, y_offset-1, x_offset)
        ChangeTile(tiles, y_offset+1, x_offset-1, y_offset-1, x_offset+1)
    
    rotation_index += 1
    if rotation_index == 4 :
        rotation_index = 0
    return rotation_index

def RotateType2(tiles, y_size, x_size, rotation_index) :
    y_offset, x_offset = FindOffset(tiles, y_size, x_size)
    if rotation_index == 0 :
        if y_offset == 0 :
            Tile.downTile(tiles, y_size, x_size)
            y_offset += 1
        ChangeTile(tiles, y_offset-1, x_offset, y_offset+1, x_offset)
        ChangeTile(tiles, y_offset+1, x_offset+1, y_offset+1, x_offset-1)
    if rotation_index == 1 :
        y_offset += 1
        if x_offset == 0 :
            Tile.rightMove(tiles, y_size, x_size)
            x_offset += 1
        ChangeTile(tiles, y_offset+1, x_offset, y_offset-1, x_offset)
        ChangeTile(tiles, y_offset+1, x_offset-1, y_offset+1, x_offset+1)
            
    if rotation_index == 0 :
        rotation_index = 1
    elif rotation_index == 1 :
        rotation_index = 0
    return rotation_index
        
def RotateType3(tiles, y_size, x_size, rotation_index) :
    y_offset, x_offset = FindOffset(tiles, y_size, x_size)
    if rotation_index == 0 :
        if y_offset >= (y_size - 2) :
            Tile.upMove(tiles, y_size, x_size)
            y_offset -= 1
        x_offset += 1
        ChangeTile(tiles, y_offset, x_offset+1, y_offset, x_offset)
        ChangeTile(tiles, y_offset+2, x_offset, y_offset, x_offset-1)
    if rotation_index == 1 :
        if x_offset == 1 :
            Tile.rightMove(tiles, y_size, x_size)
            x_offset += 1
        ChangeTile(tiles, y_offset, x_offset-2, y_offset, x_offset)
        ChangeTile(tiles, y_offset, x_offset-1, y_offset+2, x_offset-1)

    if rotation_index == 0 :
        rotation_index = 1
    elif rotation_index == 1 :
        rotation_index = 0
    return rotation_index

def RotateType4(tiles, y_size, x_size, rotation_index) :
    y_offset, x_offset = FindOffset(tiles, y_size, x_size)
    if rotation_index == 0 :
        if y_offset >= (y_size - 2) :
            Tile.upMove(tiles, y_size, x_size)
            y_offset -= 1
        ChangeTile(tiles, y_offset+2, x_offset, y_offset+1, x_offset-1)
    if rotation_index == 1 :
        if x_offset == 0 :
            Tile.rightMove(tiles, y_size, x_size)
            x_offset += 1
        ChangeTile(tiles, y_offset+1, x_offset-1, y_offset, x_offset)
    if rotation_index == 2 :
        if y_offset == 0 :
            Tile.downTile(tiles, y_size, x_size)
            y_offset += 1
        ChangeTile(tiles, y_offset-1, x_offset+1, y_offset, x_offset+2)
    if rotation_index == 3 :
        if x_offset >= (x_size - 1) :
            Tile.leftMove(tiles, y_size, x_size)
            x_offset -= 1
        ChangeTile(tiles, y_offset+1, x_offset+1, y_offset+2, x_offset)
    
    rotation_index += 1
    if rotation_index == 4 :
        rotation_index = 0
    return rotation_index

def RotateType5(tiles, y_size, x_size, rotation_index) :
    y_offset, x_offset = FindOffset(tiles, y_size, x_size)
    if rotation_index == 0 :
        if y_offset >= (y_size - 2) :
            Tile.upMove(tiles, y_size, x_size)
            y_offset -= 1
        ChangeTile(tiles, y_offset, x_offset+1, y_offset+1, x_offset+1)
        ChangeTile(tiles, y_offset+2, x_offset, y_offset+1, x_offset+2)
    if rotation_index == 1 :
        if x_offset == 0 :
            Tile.rightMove(tiles, y_size, x_size)
            x_offset += 1
        ChangeTile(tiles, y_offset+1, x_offset+1, y_offset+1, x_offset)
        ChangeTile(tiles, y_offset, x_offset-1, y_offset+2, x_offset)
    if rotation_index == 2 :
        if y_offset == 0 :
            Tile.downTile(tiles, y_size, x_size)
            y_offset += 1
        x_offset += 2
        ChangeTile(tiles, y_offset-1, x_offset, y_offset+1, x_offset)
        ChangeTile(tiles, y_offset-2, x_offset, y_offset, x_offset-2)
    if rotation_index == 3 :
        if x_offset >= (x_size - 2) :
            for i in range(x_offset - (x_size-2) + 1) :
                Tile.leftMove(tiles, y_size, x_size)
                x_offset -= 1
        ChangeTile(tiles, y_offset+2, x_offset+1, y_offset+2, x_offset-1)
        ChangeTile(tiles, y_offset+2, x_offset+2, y_offset, x_offset)
    
    rotation_index += 1
    if rotation_index == 4 :
        rotation_index = 0
    return rotation_index
