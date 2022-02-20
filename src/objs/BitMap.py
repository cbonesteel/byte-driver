import pygame
import csv
import numpy as np
from ..utils.spritesheet import SpriteSheet
from .game_object import GameObject
from pygame.math import Vector2

class BitMap:

    def __init__(self, width, height):
        self.width, self.height = width, height

        self.map = [[0 for x in range(self.width)] for y in range(self.height)]
        self.final_img = pygame.Surface((self.width*80,self.height*80)).convert_alpha()
        #Spritesheet
        self.bitmap_ss = SpriteSheet("imgs/bitmap.png")
        self.tiles = []

        for x in range(3):
            tile_rect = (0,0,80,80)
            if(x!=0):
                tile_rect = ((tile_rect[0]),(tile_rect[1]+tile_rect[3])*x,tile_rect[2],tile_rect[3])
            self.tiles += self.bitmap_ss.load_strip(tile_rect, 6, 0)



        blanktile_img = GameObject(Vector2(0,0), angle=0, scale=1, image=self.tiles[0])
        grasstile_img = GameObject(Vector2(0,0), angle=0, scale=1, image=self.tiles[1])

        rightwall_img = GameObject(Vector2(0,0), angle=0, scale=1, image=self.tiles[2])
        bottomrightcorner_img = GameObject(Vector2(0,0), angle=0, scale=1, image=self.tiles[3])

        vertroad_img = GameObject(Vector2(0,0), angle=0, scale=1, image=self.tiles[6])

        grid_img = GameObject(Vector2(0,0), angle=0, scale=1, image=self.tiles[12])
        finish_img = GameObject(Vector2(0,0), angle=0, scale=1, image=self.tiles[9])

        topleftturn_img = GameObject(Vector2(0,0), angle=0, scale=1, image=self.tiles[7])
        toprightturn_img = GameObject(Vector2(0,0), angle=0, scale=1, image=self.tiles[8])
        bottomleftturn_img = GameObject(Vector2(0,0), angle=0, scale=1, image=self.tiles[13])
        bottomrightturn_img = GameObject(Vector2(0,0), angle=0, scale=1, image=self.tiles[14])

        # set Map
        self.load_map()

        #print(str(len(list(self.map[0]))) +" " + str(len(list(self.map))))
        for i in range(len(list(self.map))):
            for j in range(len(list(self.map[i]))):
                #NULL
                if self.map[i][j] == 0:
                    self.final_img.blit(blanktile_img.surface, (j*80, i*80))
                #GRASS
                elif self.map[i][j] == 1:
                    self.final_img.blit(grasstile_img.surface, (j*80, i*80))
                #WALL
                elif self.map[i][j] == 2:
                    self.final_img.blit(rightwall_img.surface, (j*80, i*80))
                elif self.map[i][j] == 3:
                    rightwall_img.rotate(90)
                    self.final_img.blit(rightwall_img.surface, (j*80, i*80))
                    rightwall_img.rotate(-90)
                elif self.map[i][j] == 4:
                    rightwall_img.rotate(180)
                    self.final_img.blit(rightwall_img.surface, (j*80, i*80))
                    rightwall_img.rotate(-180)
                elif self.map[i][j] == 5:
                    rightwall_img.rotate(270)
                    self.final_img.blit(rightwall_img.surface, (j*80, i*80))
                    rightwall_img.rotate(-270)
                #CORNERS
                elif self.map[i][j] == 6:
                    self.final_img.blit(bottomrightcorner_img.surface, (j*80, i*80))
                elif self.map[i][j] == 7:
                    bottomrightcorner_img.rotate(90)
                    self.final_img.blit(bottomrightcorner_img.surface, (j*80, i*80))
                    bottomrightcorner_img.rotate(-90)
                elif self.map[i][j] == 8:
                    bottomrightcorner_img.rotate(180)
                    self.final_img.blit(bottomrightcorner_img.surface, (j*80, i*80))
                    bottomrightcorner_img.rotate(-180)
                elif self.map[i][j] == 9:
                    bottomrightcorner_img.rotate(270)
                    self.final_img.blit(bottomrightcorner_img.surface, (j*80, i*80))
                    bottomrightcorner_img.rotate(-270)
                #VERT ROAD
                elif self.map[i][j] == 10:
                    self.final_img.blit(vertroad_img.image, (j*80, i*80))
                #HORZ ROAD
                elif self.map[i][j] == 11:
                    vertroad_img.rotate(90)
                    self.final_img.blit(vertroad_img.image, (j*80, i*80))
                    vertroad_img.rotate(-90)
                #GRID
                elif self.map[i][j] == 12:
                    self.final_img.blit(grid_img.surface, (j*80, i*80))
                elif self.map[i][j] == 13:
                    grid_img.rotate(90)
                    self.final_img.blit(grid_img.surface, (j*80, i*80))
                    grid_img.rotate(-90)
                #FINISH
                elif self.map[i][j] == 14:
                    self.final_img.blit(finish_img.surface, (j*80, i*80))
                elif self.map[i][j] == 15:
                    grid_img.rotate(90)
                    self.final_img.blit(finish_img.surface, (j*80, i*80))
                    grid_img.rotate(-90)
                #TURN BOTTOM TO RIGHT
                elif self.map[i][j] == 16:
                    self.final_img.blit(topleftturn_img.surface, (j*80, i*80))
                elif self.map[i][j] == 17:
                    self.final_img.blit(toprightturn_img.surface, (j*80, i*80))
                elif self.map[i][j] == 18:
                    self.final_img.blit(bottomleftturn_img.surface, (j*80, i*80))
                elif self.map[i][j] == 19:
                    self.final_img.blit(bottomrightturn_img.surface, (j*80, i*80))
                #TURN LEFT TO BOTTOM
                elif self.map[i][j] == 20:
                    bottomleftturn_img.rotate(90)
                    self.final_img.blit(bottomleftturn_img.surface, (j * 80, i * 80))
                    bottomleftturn_img.rotate(-90)
                elif self.map[i][j] == 21:
                    topleftturn_img.rotate(90)
                    self.final_img.blit(topleftturn_img.surface, (j * 80, i * 80))
                    topleftturn_img.rotate(-90)
                elif self.map[i][j] == 22:
                    bottomrightturn_img.rotate(90)
                    self.final_img.blit(bottomrightturn_img.surface, (j * 80, i * 80))
                    bottomrightturn_img.rotate(-90)
                elif self.map[i][j] == 23:
                    toprightturn_img.rotate(90)
                    self.final_img.blit(toprightturn_img.surface, (j * 80, i * 80))
                    toprightturn_img.rotate(-90)
                #TURN LEFT TO TOP
                elif self.map[i][j] == 24:
                    bottomrightturn_img.rotate(180)
                    self.final_img.blit(bottomrightturn_img.surface, (j * 80, i * 80))
                    bottomrightturn_img.rotate(-180)
                elif self.map[i][j] == 25:
                    bottomleftturn_img.rotate(180)
                    self.final_img.blit(bottomleftturn_img.surface, (j * 80, i * 80))
                    bottomleftturn_img.rotate(-180)
                elif self.map[i][j] == 26:
                    toprightturn_img.rotate(180)
                    self.final_img.blit(toprightturn_img.surface, (j * 80, i * 80))
                    toprightturn_img.rotate(-180)
                elif self.map[i][j] == 27:
                    topleftturn_img.rotate(180)
                    self.final_img.blit(topleftturn_img.surface, (j * 80, i * 80))
                    topleftturn_img.rotate(-180)
                # TURN TOP TO RIGHT
                elif self.map[i][j] == 28:
                    toprightturn_img.rotate(-90)
                    self.final_img.blit(toprightturn_img.surface, (j * 80, i * 80))
                    toprightturn_img.rotate(90)
                elif self.map[i][j] == 29:
                    bottomrightturn_img.rotate(-90)
                    self.final_img.blit(bottomrightturn_img.surface, (j * 80, i * 80))
                    bottomrightturn_img.rotate(90)
                elif self.map[i][j] == 30:
                    topleftturn_img.rotate(-90)
                    self.final_img.blit(topleftturn_img.surface, (j * 80, i * 80))
                    topleftturn_img.rotate(90)
                elif self.map[i][j] == 31:
                    bottomleftturn_img.rotate(-90)
                    self.final_img.blit(bottomleftturn_img.surface, (j * 80, i * 80))
                    bottomleftturn_img.rotate(90)
                    


    def get_at(self, index1, index2):
        return map[index1, index2]

    def map0(self):
        self.map = [[1, 10, 1],
                    [1, 10, 1],
                    [1, 10, 1],
                    [11,11,11],
                    [1,1,1]]

    def load_map(self):
        self.map = np.loadtxt(open("bitmaps/austria.csv"), delimiter=",")


    def getfinalimage(self):
        return self.final_img


