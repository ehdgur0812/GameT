import pygame
import time
import Tile
import TileRotation
import TileCheck
import Information
import Tetris
import GoHero
import os
import sys
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
x_speed = 20
y_speed = 20

stage_str = "stage" 
game_stage = 1

x_line, y_line = Information.GetXYSize()
        
pygame.init()
screen = pygame.display.set_mode([1100, 600])
pygame.display.set_caption('CMSC 150 is cool')
clock = pygame.time.Clock()

pygame.mixer.music.load('sound/dark.ogg')
pygame.mixer.music.play(-1)

background_image = pygame.image.load("DarkBG.png").convert()
block_image = ["block\general.png", "block\genadd.png", "block\general.png",
                "block\general.png", "block\genbet.png", "block\general.png",
               "block\general.png", "block\gengoal.png", "block\genbad.png"]

block_list = list()
for index in range(9) :
    block_list.append(pygame.image.load(block_image[index]).convert())
    block_list[index].set_colorkey((0,0,0))

tiles = list()
for y_index in range(y_line) :
    tiles.append(list())
    for x_index in range(x_line) :
        tiles[y_index].append(Tile.TileClass())
        tiles[y_index][x_index].initTile(y_index, x_index, pygame)

def load_File(path) :
    file = open(path, "r")
    line = file.readlines()
    for y_index in range(y_line) :
        x_count = 0
        for x_index in range(x_line*2) :
            if x_index % 2 == 0 :
                if line[y_index][x_index] == '1' :
                    tiles[y_index][x_count].setBlock(1)
                if line[y_index][x_index] == '5' :
                    tiles[y_index][x_count].setBlock(5)
                if line[y_index][x_index] == '8' :
                    tiles[y_index][x_count].setBlock(8)
                if line[y_index][x_index] == '9' :
                    tiles[y_index][x_count].setBlock(9)
                x_count += 1
    file.close()

logo_image = pygame.image.load('hero/logo/Jenny_special1.png').convert()
logo_image.set_colorkey((0,0,0))
def play_Logo() :
    frame_time = 0.2
    logo_image = pygame.image.load('hero/logo/Jenny_special1.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_special2.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_special3.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_special4.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_special5.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_special6.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_special7.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_special8.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_special9.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_special10.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_attack1.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_attack2.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_attack3.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_attack4.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_attack5.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_attack6.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_attack7.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_sound = pygame.mixer.Sound('sound/logo.wav')
    pygame.mixer.Sound.play(logo_sound)
    logo_image = pygame.image.load('hero/logo/Jenny_dead1.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_dead2.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_dead3.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_dead4.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_dead5.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_dead6.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    logo_image = pygame.image.load('hero/logo/Jenny_dead7.png').convert()
    logo_image.set_colorkey((0,0,0))
    screen.blit(background_image, [0,0])
    screen.blit(logo_image, [450,250])
    pygame.display.flip()
    clock.tick(60)
    time.sleep(frame_time)
    #play_Game()
    play_Menu()

def play_Menu() :
    game_btn = pygame.image.load('game_btn.png').convert()
    game_btn.set_colorkey((0,0,0))
    select_btn = pygame.image.load('select_btn.png').convert()
    select_btn.set_colorkey((0,0,0))
    start_btn = pygame.image.load('start_btn.png').convert()
    start_btn.set_colorkey((0,0,0))
    exit_btn = pygame.image.load('exit_btn.png').convert()
    exit_btn.set_colorkey((0,0,0))

    menu_state = True
    menu_select = 1
    
    while menu_state :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_state = False
                menu_select = 0
                break
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_DOWN :
                    menu_select += 1
                    if menu_select == 3 :
                        menu_select = 1
                    break
                if event.key == pygame.K_UP :
                    menu_select -= 1
                    if menu_select == 0 :
                        menu_select = 2
                    break
                if event.key == pygame.K_SPACE :
                    menu_state = False
                    break
                
        screen.blit(background_image, [0,0])
        screen.blit(game_btn, [250, 25])
        if menu_select == 1 :
            screen.blit(select_btn, [350, 260])
        if menu_select == 2 :
            screen.blit(select_btn, [350, 420])
        screen.blit(start_btn, [450, 260])
        screen.blit(exit_btn, [450, 420])
        pygame.display.flip()
        clock.tick(60)

    exit_sound = pygame.mixer.Sound('sound/exit.wav')
    pygame.mixer.Sound.play(exit_sound)
    
    if menu_select == 1 :
        play_Game()
    #for i in range(10) :
        #os.system('start')
    
    
def play_Game() :
    global stage_str, game_stage
    now_time = time.time()
    down_time = time.time() + 0.5
    frame_time = now_time + 1.0
    frame_count = 0
    
    game_state = False
    game_number = 0

    Tetris.init_Tetris(pygame, tiles, y_line, x_line)
    stage_str += ("\\stage" + str(game_stage) + ".txt")
    load_File(stage_str)

    pygame.mixer.music.load('sound/GameBG.wav')
    pygame.mixer.music.play(-1)

    GoHero.set_HeroImage(pygame)

    while not game_state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = True
                break
            else :
                pygame.event.post(event)

        frame_count += 1
        now_time = time.time()
        if now_time >= frame_time :
            print(frame_count)
            frame_count = 0
            frame_time = now_time + 1.0
        
        if game_number == 0 :
            down_time, game_number = Tetris.play_Tetris(pygame, tiles,
                    y_line, x_line, now_time, down_time)
        elif game_number == 1 :
            game_number = GoHero.play_Hero(pygame, tiles, y_line, x_line, now_time)
        elif game_number == 9 :
            Tetris.init_Tetris(pygame, tiles, y_line, x_line)
            stage_str = "stage"
            game_stage+=1
            if game_stage == 4 :
                game_stage = 1
            stage_str += ("\\stage" + str(game_stage) + ".txt")
            load_File(stage_str)
            game_number = 0
            
        screen.blit(background_image, [0,0])
        for y_index in range(y_line) :
            for x_index in range(x_line) :
                if tiles[y_index][x_index].block != 0 :
                    screen.blit(block_list[tiles[y_index][x_index].block-1],
                                [tiles[y_index][x_index].x_position,
                                 tiles[y_index][x_index].y_position])
        #screen.blit(hero_image, hero_position)
        GoHero.draw_Hero(screen, now_time)
     
        pygame.display.flip()
        clock.tick(60)

play_Logo()
#play_Game()
 
pygame.quit()
