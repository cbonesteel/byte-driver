import pygame
from ..utils.spritesheet import SpriteSheet

class BitMap:

    def __init__(self, width, height):
        self.width, self.height = width, height

        self.map = [[0 for x in range(self.width)] for y in range(self.height)]

        self.final_img = pygame.Surface((self.width*80,self.height*80)).convert_alpha()
        #Spritesheet
        self.bitmap_ss = SpriteSheet("src/imgs/bitmap_prototype.png")
        self.tiles = []

        for x in range(2):
            tile_rect = (0,0,80,80)
            if(x!=0):
                tile_rect = ((tile_rect[0]),(tile_rect[1]+tile_rect[3])*x,tile_rect[2],tile_rect[3])
            self.tiles += self.bitmap_ss.load_strip(tile_rect, 6, 0)

        blanktile_img = self.tiles[0]
        grasstile_img = self.tiles[1]
        rightwall_img = self.tiles[2]
        vertroad_img = self.tiles[6]

        # set Map
        self.map0()

        for i in range(len(list(self.map[0]))):
            for j in range(len(list(self.map))):
                if self.map[i][j] == 1:
                    self.final_img.blit(grasstile_img, (j*80, i*80))
                    #self.final_img.load(grasstile_img, i*80, j*80)
                if self.map[i][j] == 6:
                    self.final_img.blit(vertroad_img, (j*80, i*80))


    def get_at(self, index1, index2):
        return map[index1, index2]

    def map0(self):
        self.map = [[1, 6, 1],
                    [1, 6, 1],
                    [1, 6, 1]]

    def getfinalimage(self):
        return self.final_img


