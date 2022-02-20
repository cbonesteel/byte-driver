import pygame
from ..utils.spritesheet import SpriteSheet
from .game_object import GameObject
from pygame.math import Vector2
import math

class Car(GameObject):
    def __init__(self, pos_x, pos_y, color=0, globScale=1, angle=90):
        #current animation frame
        self.anim_timer = 0
        self.anim_index = 0

        #load in spritesheet
        car_ss = SpriteSheet("./imgs/new_car.png")
        self.sprites = []

        #load in all the sprites
        car_rect = (0,0,16,32)
        self.sprites = car_ss.load_strip(car_rect, 2)
        car_img = self.sprites[self.anim_index]

        #position and direction & speed
        self.angle_change = 0
        self.direction = Vector2(math.cos(math.radians(angle+90)), math.sin(math.radians(angle+90))) # downward vector bc thats how the sprite spawns
        self.speed = 0
        self.accel = False
        self.maxSpeed = 300
        self.brake = False
        self.slowDown = False
        self.slowDownFactor = 200

        super().__init__(Vector2(pos_x, pos_y), angle=angle, scale=globScale, image=car_img)

    def animate(self, deltaTime):
        self.anim_timer += deltaTime
        if self.anim_timer > 0.07 and self.speed > 0: #after 70ms
            self.anim_timer = 0  # Reset the timer.
            self.anim_index += 1  # Increment the index.
            self.anim_index %= len(self.sprites)  # Modulo to cycle the index.
            self.update_surface(self.sprites[self.anim_index])

    def update(self, deltaTime):
        if self.angle_change != 0 and self.speed > 0:
            self.direction.rotate_ip(self.angle_change)
            self.rotate(-self.angle_change)
        #accel bool
        if self.accel:
            #increase the speed
            self.speed += 60 * deltaTime
            #slow down if we are in sand/grass
            if self.slowDown:
                if self.speed > self.maxSpeed-self.slowDownFactor:
                    self.speed = self.maxSpeed-self.slowDownFactor
            else:
                if self.speed > self.maxSpeed:
                    self.speed = self.maxSpeed
        else:
            #decrease the speed
            if self.slowDown:
                self.speed -= self.slowDownFactor * deltaTime
            else:
                self.speed -= 80 * deltaTime
            
            if self.speed < 0:
                self.speed = 0

        #truncate speed
        

        #brake bool
        if self.brake:
            self.speed -= 100 * deltaTime
            if self.speed < 0:
                self.speed = 0
        #update the positon vector and the rect
        self.move(self.direction * self.speed * deltaTime)
        self.animate(deltaTime)
    """
    def move
    def rotate
    def update
    """
    
