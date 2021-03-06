import pygame
from ..utils.spritesheet import SpriteSheet
from .game_object import GameObject
from pygame.math import Vector2
import math

class BitMap:

    def __init__(self, width, height, filename, globScale=1):
        self.width, self.height = width, height
        self.spriteWidth = 80 * globScale
        self.filename = filename

        self.map = [[0 for x in range(self.width)] for y in range(self.height)]
        self.final_img = pygame.Surface((self.width*self.spriteWidth,self.height*self.spriteWidth)).convert_alpha()
        #Spritesheet
        self.bitmap_ss = SpriteSheet("imgs/bitmap.png")
        self.tiles = []

        for x in range(3):
            tile_rect = (0,0,80,80)
            if(x!=0):
                tile_rect = ((tile_rect[0]),(tile_rect[1]+tile_rect[3])*x,tile_rect[2],tile_rect[3])
            self.tiles += self.bitmap_ss.load_strip(tile_rect, 6, 0)


        blanktile_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[0])
        grasstile_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[1])

        rightwall_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[2])
        bottomrightcorner_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[3])

        vertroad_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[6])

        grid_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[12])
        finish_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[9])

        topleftturn_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[7])
        toprightturn_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[8])
        bottomleftturn_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[13])
        bottomrightturn_img = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[14])

        self.wallGroup = []

        # set Map
        self.load_map()

        #print(str(len(list(self.map[0]))) +" " + str(len(list(self.map))))
        for i in range(len(list(self.map))):
            for j in range(len(list(self.map[i]))):
                #This is the current Sprite index that we are loading
                currSprite =(j*self.spriteWidth, i*self.spriteWidth)
                #NULL
                if self.map[i][j] == 0:
                    self.final_img.blit(blanktile_img.image, currSprite)
                #GRASS
                elif self.map[i][j] == 1:
                    self.final_img.blit(grasstile_img.image, currSprite)
                #WALL
                elif self.map[i][j] == 2:
                    #wall right
                    rightWall_img_cpy = GameObject(Vector2(currSprite[0]+40*globScale,currSprite[1]+40*globScale), angle=0, scale=globScale, image=self.tiles[2])
                    mask_surface = pygame.Surface((self.spriteWidth, self.spriteWidth)).convert_alpha()
                    mask_surface.fill((0,0,0,0))
                    mask_surface.fill(pygame.Color("white"), (60*globScale,0,20*globScale,80*globScale))
                    rightWall_img_cpy.mask = pygame.mask.from_surface(mask_surface)
                    self.wallGroup.append(rightWall_img_cpy)
                    self.final_img.blit(rightWall_img_cpy.image, currSprite)
                elif self.map[i][j] == 3:
                    #wall bottom
                    rightWall_img_cpy = GameObject(Vector2(currSprite[0]+40*globScale,currSprite[1]+40*globScale), angle=-90, scale=globScale, image=self.tiles[2])
                    mask_surface = pygame.Surface((self.spriteWidth, self.spriteWidth)).convert_alpha()
                    mask_surface.fill((0,0,0,0))
                    mask_surface.fill(pygame.Color("white"), (0,60*globScale,80*globScale,80*globScale))
                    rightWall_img_cpy.mask = pygame.mask.from_surface(mask_surface)
                    self.wallGroup.append(rightWall_img_cpy)
                    self.final_img.blit(rightWall_img_cpy.image, currSprite)
                elif self.map[i][j] == 4:
                    #wall left
                    rightWall_img_cpy = GameObject(Vector2(currSprite[0]+40*globScale,currSprite[1]+40*globScale), angle=180, scale=globScale, image=self.tiles[2])
                    mask_surface = pygame.Surface((self.spriteWidth, self.spriteWidth)).convert_alpha()
                    mask_surface.fill((0,0,0,0))
                    mask_surface.fill(pygame.Color("white"), (0,0,20*globScale,80*globScale))
                    rightWall_img_cpy.mask = pygame.mask.from_surface(mask_surface)
                    self.wallGroup.append(rightWall_img_cpy)
                    self.final_img.blit(rightWall_img_cpy.image, currSprite)
                elif self.map[i][j] == 5:
                    #wall top
                    rightWall_img_cpy = GameObject(Vector2(currSprite[0]+40*globScale,currSprite[1]+40*globScale), angle=-270, scale=globScale, image=self.tiles[2])
                    mask_surface = pygame.Surface((self.spriteWidth, self.spriteWidth)).convert_alpha()
                    mask_surface.fill((0,0,0,0))
                    mask_surface.fill(pygame.Color("white"), (0,0,80*globScale,20*globScale))
                    rightWall_img_cpy.mask = pygame.mask.from_surface(mask_surface)
                    self.wallGroup.append(rightWall_img_cpy)
                    self.final_img.blit(rightWall_img_cpy.image, currSprite)
                #CORNERS
                elif self.map[i][j] == 6:
                    #bottom right corner
                    rightWall_img_cpy = GameObject(Vector2(currSprite[0]+40*globScale,currSprite[1]+40*globScale), angle=0, scale=globScale, image=self.tiles[3])
                    mask_surface = pygame.Surface((self.spriteWidth, self.spriteWidth)).convert_alpha()
                    mask_surface.fill((0,0,0,0))
                    mask_surface.fill(pygame.Color("white"), (60*globScale,0,20*globScale,80*globScale))
                    mask_surface.fill(pygame.Color("white"), (0,60*globScale,80*globScale,80*globScale))
                    rightWall_img_cpy.mask = pygame.mask.from_surface(mask_surface)
                    self.wallGroup.append(rightWall_img_cpy)
                    self.final_img.blit(rightWall_img_cpy.image, currSprite)
                elif self.map[i][j] == 7:
                    #bottom left corner
                    rightWall_img_cpy = GameObject(Vector2(currSprite[0]+40*globScale,currSprite[1]+40*globScale), angle=-90, scale=globScale, image=self.tiles[3])
                    mask_surface = pygame.Surface((self.spriteWidth, self.spriteWidth)).convert_alpha()
                    mask_surface.fill((0,0,0,0))
                    mask_surface.fill(pygame.Color("white"), (0,0,20*globScale,80*globScale))
                    mask_surface.fill(pygame.Color("white"), (0,60*globScale,80*globScale,80*globScale))
                    rightWall_img_cpy.mask = pygame.mask.from_surface(mask_surface)
                    self.wallGroup.append(rightWall_img_cpy)
                    self.final_img.blit(rightWall_img_cpy.image, currSprite)
                elif self.map[i][j] == 8:
                    #top left corner
                    rightWall_img_cpy = GameObject(Vector2(currSprite[0]+40*globScale,currSprite[1]+40*globScale), angle=180, scale=globScale, image=self.tiles[3])
                    mask_surface = pygame.Surface((self.spriteWidth, self.spriteWidth)).convert_alpha()
                    mask_surface.fill((0,0,0,0))
                    mask_surface.fill(pygame.Color("white"), (0,0,20*globScale,80*globScale))
                    mask_surface.fill(pygame.Color("white"), (0,0,80*globScale,20*globScale))
                    rightWall_img_cpy.mask = pygame.mask.from_surface(mask_surface)
                    self.wallGroup.append(rightWall_img_cpy)
                    self.final_img.blit(rightWall_img_cpy.image, currSprite)
                elif self.map[i][j] == 9:
                    # top right corner
                    rightWall_img_cpy = GameObject(Vector2(currSprite[0]+40*globScale,currSprite[1]+40*globScale), angle=-270, scale=globScale, image=self.tiles[3])
                    mask_surface = pygame.Surface((self.spriteWidth, self.spriteWidth)).convert_alpha()
                    mask_surface.fill((0,0,0,0))
                    mask_surface.fill(pygame.Color("white"), (60*globScale,0,20*globScale,80*globScale))
                    mask_surface.fill(pygame.Color("white"), (0,0,80*globScale,20*globScale))
                    rightWall_img_cpy.mask = pygame.mask.from_surface(mask_surface)
                    self.wallGroup.append(rightWall_img_cpy)
                    self.final_img.blit(rightWall_img_cpy.image, currSprite)
                #VERT ROAD
                elif self.map[i][j] == 10:
                    self.final_img.blit(vertroad_img.image, currSprite)
                #HORZ ROAD
                elif self.map[i][j] == 11:
                    vertroad_img.rotate(90)
                    self.final_img.blit(vertroad_img.image, currSprite)
                    vertroad_img.rotate(-90)
                #GRID
                elif self.map[i][j] == 12:
                    self.final_img.blit(grid_img.image, currSprite)
                elif self.map[i][j] == 13:
                    grid_img.rotate(90)
                    self.final_img.blit(grid_img.image, currSprite)
                    grid_img.rotate(-90)
                #FINISH
                elif self.map[i][j] == 14:
                    self.final_img.blit(finish_img.image, currSprite)
                elif self.map[i][j] == 15:
                    finish_img.rotate(90)
                    self.final_img.blit(finish_img.image, currSprite)
                    finish_img.rotate(-90)
                #TURN BOTTOM TO RIGHT
                elif self.map[i][j] == 16:
                    self.final_img.blit(topleftturn_img.image, currSprite)
                elif self.map[i][j] == 17:
                    self.final_img.blit(toprightturn_img.image, currSprite)
                elif self.map[i][j] == 18:
                    self.final_img.blit(bottomleftturn_img.image, currSprite)
                elif self.map[i][j] == 19:
                    self.final_img.blit(bottomrightturn_img.image, currSprite)
                #TURN LEFT TO BOTTOM
                elif self.map[i][j] == 20:
                    bottomleftturn_img.rotate(-90)
                    self.final_img.blit(bottomleftturn_img.image, currSprite)
                    bottomleftturn_img.rotate(90)
                elif self.map[i][j] == 21:
                    topleftturn_img.rotate(-90)
                    self.final_img.blit(topleftturn_img.image, currSprite)
                    topleftturn_img.rotate(90)
                elif self.map[i][j] == 22:
                    bottomrightturn_img.rotate(-90)
                    self.final_img.blit(bottomrightturn_img.image, currSprite)
                    bottomrightturn_img.rotate(90)
                elif self.map[i][j] == 23:
                    toprightturn_img.rotate(-90)
                    self.final_img.blit(toprightturn_img.image, currSprite)
                    toprightturn_img.rotate(90)
                #TURN LEFT TO TOP
                elif self.map[i][j] == 24:
                    bottomrightturn_img.rotate(180)
                    self.final_img.blit(bottomrightturn_img.image, currSprite)
                    bottomrightturn_img.rotate(-180)
                elif self.map[i][j] == 25:
                    bottomleftturn_img.rotate(180)
                    self.final_img.blit(bottomleftturn_img.image, currSprite)
                    bottomleftturn_img.rotate(-180)
                elif self.map[i][j] == 26:
                    toprightturn_img.rotate(180)
                    self.final_img.blit(toprightturn_img.image, currSprite)
                    toprightturn_img.rotate(-180)
                elif self.map[i][j] == 27:
                    topleftturn_img.rotate(180)
                    self.final_img.blit(topleftturn_img.image, currSprite)
                    topleftturn_img.rotate(-180)
                # TURN TOP TO RIGHT
                elif self.map[i][j] == 28:
                    toprightturn_img.rotate(90)
                    self.final_img.blit(toprightturn_img.image, currSprite)
                    toprightturn_img.rotate(-90)
                elif self.map[i][j] == 29:
                    bottomrightturn_img.rotate(90)
                    self.final_img.blit(bottomrightturn_img.image, currSprite)
                    bottomrightturn_img.rotate(-90)
                elif self.map[i][j] == 30:
                    topleftturn_img.rotate(90)
                    self.final_img.blit(topleftturn_img.image, currSprite)
                    topleftturn_img.rotate(-90)
                elif self.map[i][j] == 31:
                    bottomleftturn_img.rotate(90)
                    self.final_img.blit(bottomleftturn_img.image, currSprite)
                    bottomleftturn_img.rotate(-90)

    def get_at(self, pos_x, pos_y):
        return self.map[int(pos_y/self.spriteWidth)][int(pos_x/self.spriteWidth)]

    def map0(self):
        self.map = [[1, 10, 1],
                    [1, 10, 1],
                    [1, 10, 1],
                    [11,11,11],
                    [1,1,1]]

    def load_map(self):
        with open(self.filename) as f:
            self.map = list(map(lambda l: list(map(int, l.split(","))), f.readlines()))


    def getfinalimage(self):
        return self.final_img


if __name__ == "__main__":
    pygame.init()
    SCREEN = WIDTH, HEIGHT = 500, 500
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)

    clock = pygame.time.Clock()
    FPS = 60
    count = 0

    bitmap = BitMap(32,26,1)

    moving_object = GameObject(Vector2(40, 40), Vector2(25, 25), 45)
    all_objs = pygame.sprite.Group([moving_object])
    background = bitmap.getfinalimage()

    rightWall_img_cpy = GameObject(Vector2(0,0), angle=0, scale=globScale, image=self.tiles[2])
    bitmap.final_img.blit(rightWall_img_cpy.image, currSprite)
    rightWall_img_cpy.mask = pygame.mask.from_threshold(rightWall_img_cpy.image, color=(215, 216, 150))
    rightWall_img_cpy.move((currSprite[0]+40, currSprite[1]+40))
    self.wallGroup.append(rightWall_img_cpy)
    static_objs = pygame.sprite.Group(static_objects)

    running = True
    while running:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        if moving_object.is_colliding(bitmap.wallGroup):
            print("yes")

        count += 1
        if count % 100 == 0:
            moving_object.rotate(20)
            count = 0
        pos = pygame.mouse.get_pos()
        moving_object.set_pos(Vector2(pos[0], pos[1]))

        win.fill((255,255,255))
        all_objs.update(dt)
        all_objs.draw(win)
        pygame.display.update()
    pygame.quit()
