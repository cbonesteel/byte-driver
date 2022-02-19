import pygame
from ..utils.spritesheet import SpriteSheet
from pygame.math import Vector2

class Car(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, color=0):
        super().__init__()
        #current animation frame
        self.anim = 0

        #load in spritesheet
        self.car_ss = SpriteSheet("src/imgs/f1_sprites_trans.png")
        self.sprites = []

        #load in all the sprites
        for x in range(4): # 4 bc there are 4 rows of sprites
            car_rect = (150,90,70,125)
            if(x!=0):
                v_offset = 25
                car_rect = (car_rect[0],(car_rect[1]+car_rect[3]+v_offset)*x,car_rect[2],car_rect[3])
            self.sprites += self.car_ss.load_strip(car_rect,6, 17)

        #create the Car
        car_img = self.sprites[color]

        #add the car as the img
        self.image = car_img
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        #rotating stuff
        self.og_img = self.image
        self.angle_change = 0
        self.angle = 0

        #position and direction & speed
        self.position = Vector2(pos_x, pos_y)
        self.direction = Vector2(0,1) # downward vector bc thats how the sprite spawns
        self.speed=0
        self.accel =False
        self.maxSpeed = 5
    def update(self):
        if self.angle_change != 0 and self.speed > 0:
            self.direction.rotate_ip(self.angle_change)
            self.angle += self.angle_change
            # I prefer rotozoom because it looks smoother.
            self.image = pygame.transform.rotozoom(self.og_img, -self.angle, 1)
            self.rect = self.image.get_rect(center=self.rect.center)
        if(self.accel == True):
            #increase the speed
            self.speed +=0.25
            if(self.speed > self.maxSpeed):
                self.speed = self.maxSpeed
        else:
            #decrease the speed
            self.speed -=0.25
            if(self.speed < 0):
                self.speed = 0
        #update the positon vector and the rect
        self.position += self.direction * self.speed
        self.rect.center = self.position
    """
    def move
    def rotate
    def update
    """
    