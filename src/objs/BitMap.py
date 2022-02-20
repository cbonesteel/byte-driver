import pygame
from ..utils.spritesheet import SpriteSheet
from .game_object import GameObject
from pygame.math import Vector2

class BitMap:

    def __init__(self, width, height, globScale=1):
        self.width, self.height = width, height
        self.spriteWidth = 80 * globScale

        self.map = [[0 for x in range(self.width)] for y in range(self.height)]
        self.final_img = pygame.Surface((self.width*self.spriteWidth,self.height*self.spriteWidth)).convert_alpha()
        #Spritesheet
        self.bitmap_ss = SpriteSheet("src/imgs/bitmap_prototype.png")
        self.tiles = []

        for x in range(2):
            tile_rect = (0,0,80,80)
            if(x!=0):
                tile_rect = ((tile_rect[0]),(tile_rect[1]+tile_rect[3])*x,tile_rect[2],tile_rect[3])
            self.tiles += self.bitmap_ss.load_strip(tile_rect, 6, 0)

        blanktile_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[0])
        grasstile_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[1])
        rightwall_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[2])
        vertroad_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[6])
        horizontalroad_img = GameObject(Vector2(0,0), angle=90, scale=globScale, image=self.tiles[6])

        # set Map
        self.map0()

        print(str(len(list(self.map[0]))) +" " + str(len(list(self.map))))
        for i in range(len(list(self.map))):
            for j in range(len(list(self.map[i]))):
                currSprite =(j*self.spriteWidth, i*self.spriteWidth)
                if self.map[i][j] == 1:
                    self.final_img.blit(grasstile_img.image, currSprite)
                    #self.final_img.load(grasstile_img, i*80, j*80)
                if self.map[i][j] == 10:
                    self.final_img.blit(vertroad_img.image, currSprite)
                if self.map[i][j] == 11:
                    self.final_img.blit(horizontalroad_img.image, currSprite)               

    def get_at(self, index1, index2):
        return map[index1, index2]

    def map0(self):
        self.map = [[1, 10, 1],
                    [1, 10, 1],
                    [1, 10, 1],
                    [11,11,11],
                    [1,1,1]]

    def getfinalimage(self):
        return self.final_img


