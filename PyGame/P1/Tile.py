import random

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
    x_position = int()
    y_position = int()
    def initTile(self, y, x, pygame) :
        self.block = 0
        self.hold = True
        self.x_position = x * 20
        self.y_position = y * 20
        self.image = pygame.image.load("block\general.png").convert()
        self.image.set_colorkey((0,0,0))
    def reInit(self) :
        self.block = 0
        self.hold = True

def randomTile(tiles) :
    randType = random.randint(0,6)
    x_offset = 10
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

def allHold(tiles, y_size, x_size) :
    for y_index in range(y_size) :
        for x_index in range(x_size) :
            tiles[y_index][x_index].hold = True

def getBlockSize(tiles, y_size, x_size) :
    blockCount = 0
    for y_index in range(y_size) :
        for x_index in range(x_size) :
            if tiles[y_index][x_index].block == 1 :
                blockCount = blockCount + 1
    return blockCount

def blockCopy(tiles, copytiles, y_size, x_size) :
    for y_index in range(y_size) :
        for x_index in range(x_size) :
            tiles[y_index][x_index].block = copytiles[y_index][x_index].block
            tiles[y_index][x_index].hold = copytiles[y_index][x_index].hold

backTiles = list()
for y_index in range(30) :
    backTiles.append(list())
    for x_index in range(20) :
        backTiles[y_index].append(TileClass())

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
    if allHoldState == True :
        allHold(tiles, y_size, x_size)
        reSetState = True
    if getBlockSize(backTiles, y_size, x_size) != getBlockSize(tiles, y_size, x_size) :
        blockCopy(tiles, backTiles, y_size, x_size)
        allHold(tiles, y_size, x_size)
        reSetState = True
    return reSetState

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

