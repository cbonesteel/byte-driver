from re import M
from tkinter.tix import MAIN
from turtle import back
import pygame, sys
from .objs.car import Car
from .objs.camera import Camera
from .settings.options import *
from .objs.BitMap import BitMap
from .utils.events import *
from .utils.menu_state import *
from .utils.game_state import *
from .utils.track_select import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    #menu stuff
    game_init = False
    menu_state = MenuState.NONE
    game_state = GameState.RUNNING
    selected_track = TrackSelect.AUSTRIA

    while True:
        delta = clock.tick(20)

        #--- EVENT HANDLER ---#
        for event in pygame.event.get():
            #--- X/ESC to QUIT ---#
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            #--- MENU EVENT CONTROLS ---#
            if event.type == MAIN_MENU:
                menu_state = MenuState.MAIN_MENU
            elif event.type == SINGLEPLAYER_MENU:
                menu_state = MenuState.TRACK_SELECT
            elif event.type == MULTIPLATER_MENU:
                menu_state = MenuState.MULTIPLAYER

            #--- GAME EVENTS ---#
            if event.type == START_SINGLEPLAYER:
                menu_state = MenuState.NONE
                game_state = GameState.RUNNING

            #--- USER CONTROLS ---#
            if game_state == GameState.RUNNING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        car1.angle_change = -5
                    elif event.key == pygame.K_RIGHT:
                        car1.angle_change = 5
                    elif event.key == pygame.K_UP:
                        car1.accel = True
                    elif event.key == pygame.K_DOWN:
                        car1.brake = True
                if event.type == pygame.KEYUP:
                    # Stop rotating if the player releases the keys.
                    if event.key == pygame.K_RIGHT and car1.angle_change > 0:
                        car1.angle_change = 0
                    elif event.key == pygame.K_LEFT and car1.angle_change < 0:
                        car1.angle_change = 0
                    elif event.key == pygame.K_UP:
                        car1.accel = False
                    elif event.key == pygame.K_DOWN:
                        car1.brake = False

        #--- MENU LOGIC ---#
        if menu_state == MenuState.MAIN_MENU:
            draw_main(screen)

        #--- GAME LOGIC ---#
        if game_state == GameState.RUNNING:
            if game_init == False:
                if selected_track == TrackSelect.AUSTRIA:
                    bitmap = BitMap(32,26,"bitmaps/austria.csv",GLOBALSCALE)
                    background = bitmap.getfinalimage()
                elif selected_track == TrackSelect.SUGNOMA:
                    bitmap = BitMap(24,30,"bitmaps/sugnoma.csv",GLOBALSCALE)
                    background = bitmap.getfinalimage()
                
                #create the sprites and groups
                camera_group = Camera(screen, background)

                #create one car
                car1 = Car(1000,1000,0, GLOBALSCALE)
                camera_group.add(car1)

                game_init = True
            
        if(car1.is_colliding(bitmap.wallGroup)):
            car1.speed=-100
            car1.accel=True
            car1.brake=False
        #current Car tile
        currTile = int(bitmap.get_at(car1.get_pos()[0],car1.get_pos()[1]))
        if(currTile >= 1 and currTile <= 9 ):
            #in sand/gas
            car1.slowDown = True
        else:
            car1.slowDown = False

        # Screen Updating
        #screen.fill((0,0,0))
        if game_state == GameState.RUNNING:
            camera_group.update(delta/1000)
            camera_group.camera_draw(car1)
        pygame.display.update()

def draw_main(screen):
    # Objects
    background = pygame.image.load("imgs/retro-background.jpg")
    background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
    title = pygame.image.load("imgs/ByteDriver_Title.png")
    title = pygame.transform.scale(title, (WINDOW_WIDTH / 2,  WINDOW_WIDTH / 2 / 3))
    singleplayer = pygame.image.load("imgs/singleplayer.png")
    singleplayer = pygame.transform.scale(singleplayer, (WINDOW_WIDTH / 3,  WINDOW_WIDTH / 3 / 3))
    multiplayer = pygame.image.load("imgs/multiplayer.png")
    multiplayer = pygame.transform.scale(multiplayer, (WINDOW_WIDTH / 3,  WINDOW_WIDTH / 3 / 3))
    quit = pygame.image.load("imgs/quit.png")
    quit = pygame.transform.scale(quit, (WINDOW_WIDTH / 3,  WINDOW_WIDTH / 3 / 3))
    version = pygame.image.load("imgs/version.png")
    version = pygame.transform.scale(version, (WINDOW_WIDTH / 3,  WINDOW_WIDTH / 3 / 3))

    # Place Objects
    screen.blit(background,(0,0))
    screen.blit(title,(WINDOW_WIDTH / 4, WINDOW_HEIGHT / 8))
    screen.blit(singleplayer,(WINDOW_WIDTH / 3, WINDOW_HEIGHT / 8 * 3))
    screen.blit(multiplayer,(WINDOW_WIDTH / 3, WINDOW_HEIGHT / 8 * 4))
    screen.blit(quit,(WINDOW_WIDTH / 3, WINDOW_HEIGHT / 8 * 5))
    screen.blit(version,(WINDOW_WIDTH / 8 * 6, WINDOW_HEIGHT / 8 * 7))


def draw_track_select():
    # TODO: TRACK SELECTION
    pass

def draw_multiplayer():
    # TODO: MULTIPLAYER
    pass
