import random
import Information

x_line, y_line = Information.GetXYSize()

blockType = list()
for types in range(7) :
    blockType.append(list())
    if types == 0 :
        for y_index in range(4) :
            blockType[types].append(list())
            for x_index in range(1) :
                blockType[types][y_index].append(0)
    elif types == 6 :
        for y_index in range(2) :
            blockType[types].append(list())
            for x_index in range(2) :
                blockType[types][y_index].append(0)
    else :
        for y_index in range(2) :
            blockType[types].append(list())
            for x_index in range(3) :
                blockType[types][y_index].append(0)
                
nT = 0
blockType[nT][0][0] = 1; blockType[nT][1][0] = 1; blockType[nT][2][0] = 1; blockType[nT][3][0] = 1; nT = nT+1;
blockType[nT][1][0] = 1; blockType[nT][1][1] = 1; blockType[nT][1][2] = 1; blockType[nT][0][2] = 1; nT = nT+1;
blockType[nT][0][1] = 1; blockType[nT][0][2] = 1; blockType[nT][1][0] = 1; blockType[nT][1][1] = 1; nT = nT+1;
blockType[nT][0][0] = 1; blockType[nT][0][1] = 1; blockType[nT][1][1] = 1; blockType[nT][1][2] = 1; nT = nT+1;
blockType[nT][0][1] = 1; blockType[nT][1][0] = 1; blockType[nT][1][1] = 1; blockType[nT][1][2] = 1; nT = nT+1;
blockType[nT][0][0] = 1; blockType[nT][1][0] = 1; blockType[nT][1][1] = 1; blockType[nT][1][2] = 1; nT = nT+1;
blockType[nT][0][0] = 1; blockType[nT][1][0] = 1; blockType[nT][1][1] = 1; blockType[nT][0][1] = 1; nT = nT+1;

class TileClass :
    block = int()
    hold = bool()
    ghost = bool()
    x_position = int()
    y_position = int()
    def initTile(self, y, x, pygame) :
        self.block = 0
        self.hold = True
        ghost = False
        self.x_position = x * 20
        self.y_position = y * 20
        self.image = pygame.image.load("block\general.png").convert()
        self.image.set_colorkey((0,0,0))
    def reInit(self) :
        self.block = 0
        self.hold = True
    def setBlock(self, block_type) :
        self.block = block_type
        self.hold = True

def randomTile(tiles) :
    randType = random.randint(0,6)
    #randType = 5
    x_offset = 2
    y_offset = 0
    if randType == 0 :
        for y_index in range(4) :
            tiles[y_offset + y_index][x_offset - 1].block = blockType[randType][y_index][0]
            if tiles[y_offset + y_index][x_offset - 1].block == 1 :
                tiles[y_offset + y_index][x_offset - 1].hold = False
    elif randType == 6 :
        for y_index in range(2) :
            for x_index in range(2) :
                tiles[y_offset + y_index][x_offset + x_index - 1].block = blockType[randType][y_index][x_index]
                if tiles[y_offset + y_index][x_offset + x_index - 1].block == 1 :
                    tiles[y_offset + y_index][x_offset + x_index - 1].hold = False
    else :
        for y_index in range(2) :
            for x_index in range(3) :
                tiles[y_offset + y_index][x_offset + x_index - 2].block = blockType[randType][y_index][x_index]
                if tiles[y_offset + y_index][x_offset + x_index - 2].block == 1 :
                    tiles[y_offset + y_index][x_offset + x_index - 2].hold = False
    return randType

def allHold(tiles, y_size, x_size) :
    for y_index in range(y_size) :
        for x_index in range(x_size) :
            tiles[y_index][x_index].hold = True

def getBlockSize(tiles, y_size, x_size) :
    blockCount = 0
    for y_index in range(y_size) :
        for x_index in range(x_size) :
            if tiles[y_index][x_index].block != 0 and tiles[y_index][x_index].block != 2 :
                blockCount = blockCount + 1
    return blockCount

def blockCopy(tiles, copytiles, y_size, x_size) :
    for y_index in range(y_size) :
        for x_index in range(x_size) :
            tiles[y_index][x_index].block = copytiles[y_index][x_index].block
            tiles[y_index][x_index].hold = copytiles[y_index][x_index].hold

def notNeedInit(tiles, y_size, x_size) :
    for y_index in range(y_size) :
        for x_index in range(x_size) :
            if tiles[y_index][x_index].block == 1 and tiles[y_index][x_index].hold == False :
                tiles[y_index][x_index].reInit()
            if tiles[y_index][x_index].block == 2 :
                tiles[y_index][x_index].reInit()

backTiles = list()
ghostTiles = list()
for y_index in range(y_line) :
    backTiles.append(list())
    ghostTiles.append(list())
    for x_index in range(x_line) :
        ghostTiles[y_index].append(TileClass())
        backTiles[y_index].append(TileClass())

allHoldState = False
def getHoldState() :
    global allHoldState
    return allHoldState
def downTile(tiles, y_size, x_size) :
    blockCopy(backTiles, tiles, y_size, x_size)
    allHoldState = False
    reSetState = False
    for y_index in range(y_size) :
        for x_index in range(x_size) :
            ry = y_size - y_index - 1
            rx = x_size - x_index - 1
            if ry == 0 and tiles[ry][rx].hold == False :
                tiles[ry][rx].reInit()
            elif tiles[ry-1][rx].hold == False and tiles[ry-1][rx].block == 1 and ry != 0:
                tiles[ry][rx].hold = False
                tiles[ry][rx].block = tiles[ry-1][rx].block
            elif tiles[ry-1][rx].hold == True and tiles[ry][rx].hold == False :
                tiles[ry][rx].reInit()
            if ry == (y_size-1) and tiles[ry][rx].block == 1 and tiles[ry][rx].hold == False:
                allHoldState = True
    #if allHoldState == True :
        #allHold(tiles, y_size, x_size)
        #reSetState = True
    if getBlockSize(backTiles, y_size, x_size) != getBlockSize(tiles, y_size, x_size) :
        blockCopy(tiles, backTiles, y_size, x_size)
        allHold(tiles, y_size, x_size)
        reSetState = True
    return reSetState

def upMove(tiles, y_size, x_size) :
    blockCopy(backTiles, tiles, y_size, x_size)
    for y_index in range(y_size) :
        for x_index in range(x_size) :
            if tiles[y_index][x_index].block == 1 and tiles[y_index][x_index].hold == False :
                tiles[y_index-1][x_index].block = tiles[y_index][x_index].block
                tiles[y_index-1][x_index].hold = tiles[y_index][x_index].hold
                tiles[y_index][x_index].reInit()
    if getBlockSize(backTiles, y_size, x_size) != getBlockSize(tiles, y_size, x_size) :
        blockCopy(tiles, backTiles, y_size, x_size)

def leftMove(tiles, y_size, x_size) :
    blockCopy(backTiles, tiles, y_size, x_size)
    for y_index in range(y_size) :
        for x_index in range(x_size) :
            if tiles[y_index][x_index].block == 1 and tiles[y_index][x_index].hold == False :
                if (x_index-1) >= 0 :
                    tiles[y_index][x_index-1].block = tiles[y_index][x_index].block
                    tiles[y_index][x_index-1].hold = tiles[y_index][x_index].hold
                    tiles[y_index][x_index].reInit()
    if getBlockSize(backTiles, y_size, x_size) != getBlockSize(tiles, y_size, x_size) :
        blockCopy(tiles, backTiles, y_size, x_size)

def rightMove(tiles, y_size, x_size) :
    blockCopy(backTiles, tiles, y_size, x_size)
    for y_index in range(y_size) :
        for x_index in range(x_size) :
            rx = x_size - x_index - 1
            if tiles[y_index][rx].block == 1 and tiles[y_index][rx].hold == False :
                if (rx+1) <= (x_size-1) :
                    tiles[y_index][rx+1].block = tiles[y_index][rx].block
                    tiles[y_index][rx+1].hold = tiles[y_index][rx].hold
                    tiles[y_index][rx].reInit()
    if getBlockSize(backTiles, y_size, x_size) != getBlockSize(tiles, y_size, x_size) :
        blockCopy(tiles, backTiles, y_size, x_size)

def speedMove(tiles, y_size, x_size) :
    while True :
        if downTile(tiles, y_size, x_size) == True :
            break

def downTileOffset(tiles, x_start, x_end, y_start, y_end) :
    y_index = y_end
    while y_index >= y_start :
        x_index = x_start
        while x_index <= x_end :
            if tiles[y_index][x_index].block == 1 and tiles[y_index][x_index].hold == False :
                tiles[y_index+1][x_index].block = tiles[y_index][x_index].block
                tiles[y_index+1][x_index].hold = tiles[y_index][x_index].hold
                tiles[y_index][x_index].reInit()
            x_index += 1
        y_index -= 1

def alldownTile(tiles, y_size, x_start, x_end, y_start, y_end) :
    y_index = y_end
    y_offset = y_start
    down_state = True
    while y_index < y_size :
        y_offset = y_start
        while y_offset <= y_end :
            x_index = x_start
            while x_index <= x_end :
                if tiles[y_offset+1][x_index].block != 0 and tiles[y_offset+1][x_index].block != 2 and tiles[y_offset][x_index].block == 1:
                    if tiles[y_offset+1][x_index].hold == True and tiles[y_offset][x_index].hold == False:
                        down_state = False
                        break
                x_index += 1
            y_offset += 1
        if down_state == True :
            downTileOffset(tiles, x_start, x_end, y_start, y_end)
            y_start += 1
            y_end += 1
        if down_state == False :
            break
        y_index += 1

def ghostMove(tiles, y_size, x_size) :    
    blockCopy(ghostTiles, tiles, y_size, x_size)
    x_start, y_start = 0, 0
    x_end, y_end = x_size-1, y_size-1
    start_state = True
    end_state = True
    for x_index in range(x_size) :
        for y_index in range(y_size) :
            if start_state == True :
                if ghostTiles[y_index][x_index].block == 1 and ghostTiles[y_index][x_index].hold == False :
                    start_state = False
                    x_start = x_index
            if end_state == True :
                if ghostTiles[y_index][x_size - x_index - 1].block == 1 and ghostTiles[y_index][x_size - x_index - 1].hold == False :
                    end_state = False
                    x_end = x_size - x_index - 1
        if start_state == False and end_state == False :
            break
    start_state = True
    end_state = True
    for y_index in range(y_size) :
        x_index = x_start
        while x_index <= x_end:
            if start_state == True :
                if ghostTiles[y_index][x_index].block == 1 and ghostTiles[y_index][x_index].hold == False :
                    start_state = False
                    y_start = y_index
            if end_state == True :
                if ghostTiles[y_size - y_index - 1][x_index].block == 1 and ghostTiles[y_size - y_index - 1][x_index].hold == False :
                    end_state = False
                    y_end = y_size - y_index - 1
            x_index += 1
        if start_state == False and end_state == False :
            break
    alldownTile(ghostTiles, y_size, x_start, x_end, y_start, y_end)
    for y_index in range(y_size) :
        for x_index in range(x_size) :
            if tiles[y_index][x_index].block == 2 :
                tiles[y_index][x_index].block = 0
            if ghostTiles[y_index][x_index].block == 1 and tiles[y_index][x_index].block == 0 :
                tiles[y_index][x_index].block = 2
