
left_move = False
right_move = False
jump_state = True
hero_speed = 4
hero_gravity = 1.0
hero_copypos = [0,0]
x_position = [0,0]
y_position = [0,0]

hero_position = [0,540]
image_list = ["hero\Jenny_move1.png", "hero\Jenny_move2.png",
              "hero\Jenny_move3.png", "hero\Jenny_move4.png",
              "hero\Jenny_Lmove1.png", "hero\Jenny_Lmove2.png",
              "hero\Jenny_Lmove3.png", "hero\Jenny_Lmove4.png",
              "hero\Jenny_stand1.png", "hero\Jenny_stand2.png", "hero\Jenny_stand3.png",
              "hero\Jenny_stand4.png", "hero\Jenny_stand5.png"]
hero_image = list()
hero_index = 0
hero_index_time = 0.0
hero_state = 0 # move 0, lmove 1, stand 2

def set_HeroImage(pygame) :
    global hero_state, hero_index
    for index in range(13) :
        hero_image.append(pygame.image.load(image_list[index]).convert())
        hero_image[index].set_colorkey((0,0,0))
    hero_index = 8
    hero_state = 2

def change_HeroState(state) :
    global hero_state, hero_index
    hero_state = state
    if hero_state == 0 :
        hero_index = 0
    elif hero_state == 1 :
        hero_index = 4
    elif hero_state == 2 :
        hero_index = 8
    
def GoHeroInit() :
    global left_move, right_move, jump_state
    hero_position[1] = 540
    hero_position[0] = 0
    left_move = False
    right_move = False
    jump_state = False

def copyPosition(copy_position, base_position) :
    copy_position[0] = base_position[0]
    copy_position[1] = base_position[1]

def upTilePosition(hero_position) :
    global x_position, y_position
    x_position[0] = hero_position[0] / 20
    y_position[0] = hero_position[1] / 20
    x_position[0] = round(x_position[0])
    y_position[0] -= (y_position[0] % 1.0)
    y_position[0] = int(y_position[0])
    x_position[1] = x_position[0] + 1
    y_position[1] = y_position[0] + 2

def checkTileX(tiles, y_line, x_line, hero_position) :
    global hero_speed, hero_gravity
    global x_position
    y_pos = y_position[0]
    while y_pos <= (y_position[1]-1) :
        if tiles[y_pos][x_position[0]].block != 0 and tiles[y_pos][x_position[0]].block != 8 :
            hero_position[0] += hero_speed
            break
        if tiles[y_pos][x_position[1]].block != 0 and tiles[y_pos][x_position[1]].block != 8 :
            hero_position[0] -= hero_speed
            break
        y_pos += 1
def checkTileY(tiles, y_line, x_line, hero_position) :
    global x_position, y_position
    global hero_gravity
    global jump_state
    x_pos = x_position[0]
    while x_pos <= x_position[1] :
        if tiles[y_position[0]][x_pos].block != 0 and tiles[y_position[0]][x_pos].block != 8 :
            hero_position[1] += (hero_position[1] % 20)
            hero_gravity = 0.0
            break
        if tiles[y_position[1]][x_pos].block != 0 and tiles[y_position[1]][x_pos].block != 8 :
            hero_position[1] -= (hero_position[1] % 20)
            jump_state = True
            hero_gravity = 0.0
            break
        x_pos += 1
    return jump_state

def checkHeroGoal(tiles, hero_position) :
    global x_position, y_position
    upTilePosition(hero_position)
    for y_index in range(2) :
        for x_index in range(2) :
            if tiles[y_position[0] + y_index][x_position[x_index]].block == 8 :
                return True;
    return False

def draw_Hero(screen, now_time) :
    global hero_index, hero_index_time
    screen.blit(hero_image[hero_index], hero_position)
    if now_time >= hero_index_time :
        hero_index += 1
        if hero_state == 0 :
            if hero_index == 4 :
                hero_index = 0
        elif hero_state == 1 :
            if hero_index == 8 :
                hero_index = 4
        elif hero_state == 2 :
            if hero_index == 13 :
                hero_index = 8
        hero_index_time = now_time + 0.2
    
def play_Hero(pygame, tiles, y_line, x_line, now_time) :
    global left_move, right_move
    global hero_speed, hero_gravity
    global x_position, y_position
    global jump_state, hero_state

    copyPosition(hero_copypos, hero_position)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                left_move = True
                if hero_state != 1 :
                    change_HeroState(1)
            if event.key == pygame.K_RIGHT :
                right_move = True
                if hero_state != 0 :
                    change_HeroState(0)
            if event.key == pygame.K_UP and jump_state == True:
                upTilePosition(hero_copypos)
                if tiles[y_position[0]-1][x_position[0]].block == 0 :
                    if tiles[y_position[0]-1][x_position[1]].block == 0 :
                        hero_gravity = -3.3
                        jump_state = False
            if event.key == pygame.K_SPACE :
                hero_gravity = -6.3
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT :
                left_move = False
            if event.key == pygame.K_RIGHT :
                right_move = False

    if left_move == True :
        hero_copypos[0] -= hero_speed
        upTilePosition(hero_copypos)
        checkTileX(tiles, y_line, x_line, hero_copypos)
    if right_move == True :
        hero_copypos[0] += hero_speed
        upTilePosition(hero_copypos)
        checkTileX(tiles, y_line, x_line, hero_copypos)
        
    if left_move == False and right_move == False :
        if hero_state != 2 :
            change_HeroState(2)
            
    hero_copypos[1] += hero_gravity
    if hero_gravity <= 19 :
        hero_gravity += 0.3

    upTilePosition(hero_copypos)
    checkTileY(tiles, y_line, x_line, hero_copypos)
    copyPosition(hero_position, hero_copypos)
    
    if checkHeroGoal(tiles, hero_position) == True :
        GoHeroInit()
        return 9
    else :
        return 1
