import pygame
from ..utils.spritesheet import SpriteSheet
from pygame.math import Vector2

class Car(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, color=0):
        super().__init__()
        #current animation frame
        self.anim = 0

        #load in spritesheet
        self.car_ss = SpriteSheet("./imgs/new_car.png")
        self.sprites = []

        #load in all the sprites
        for x in range(4): # 4 bc there are 4 rows of sprites
            car_rect = (0,0,16,32)
            self.sprites += self.car_ss.load_strip(car_rect,2)

        #create the Car
        car_img = self.sprites[color]
        scale = 3
        car_img = pygame.transform.scale(car_img, (car_img.get_size()[0] * scale, car_img.get_size()[1] * scale))

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
        self.maxSpeed = 300
        self.brake = False
    def update(self, deltaTime):
        if self.angle_change != 0 and self.speed > 0:
            self.direction.rotate_ip(self.angle_change)
            self.angle += self.angle_change
            # I prefer rotozoom because it looks smoother.
            self.image = pygame.transform.rotozoom(self.og_img, -self.angle, 1)
            self.rect = self.image.get_rect(center=self.rect.center)
        #accel bool
        if(self.accel == True):
            #increase the speed
            self.speed +=60 * deltaTime
            if(self.speed > self.maxSpeed):
                self.speed = self.maxSpeed
        else:
            #decrease the speed
            self.speed -=40 * deltaTime
            if(self.speed < 0):
                self.speed = 0
        #brake bool
        if(self.brake):
            self.speed -= 100 * deltaTime
            if(self.speed < 0):
                self.speed = 0
        #update the positon vector and the rect
        self.position += self.direction * self.speed * deltaTime
        self.rect.center = self.position
    """
    def move
    def rotate
    def update
    """
    