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
    menu_state = MenuState.MAIN_MENU
    game_state = GameState.NONE
    selected_track = TrackSelect.NONE

    while True:
        delta = clock.tick(20)

        for event in pygame.event.get():
            #--- X to QUIT ---#
            if event.type == pygame.QUIT:
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
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif(event.key == pygame.K_LEFT):
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
                car1 = Car(100,100,0, GLOBALSCALE)
                camera_group.add(car1)

                game_init = True
            
            #current Car tile
            currTile = int(bitmap.get_at(car1.get_pos()[0],car1.get_pos()[1]))
            if(currTile >= 1 and currTile <= 9 ):
                #in sand/gas
                car1.slowDown = True
            else:
                car1.slowDown = False

        screen.fill((0,0,0))
        if game_state == GameState.RUNNING:
            camera_group.update(delta/1000)
            camera_group.camera_draw(car1)
        pygame.display.update()

    def draw_main():
        # TODO: MAIN MENU
        pass

    def draw_track_select():
        # TODO: TRACK SELECTION
        pass

    def draw_multiplayer():
        # TODO: MULTIPLAYER
        pass