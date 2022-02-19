import pygame
from pygame.math import Vector2

class SpriteSheet:
    def __init__(self, filename):
        """Load the sheet."""
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as e:
            print(f"Unable to load spritesheet image: {filename}")
            raise SystemExit(e)


    def image_at(self, rectangle, colorkey = None):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey = None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey = None):
        """Load a whole strip of images, and return them as a list."""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

class Car(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        #current animation frame
        self.anim = 0

        #load in spritesheet
        self.car_ss = SpriteSheet("src/imgs/f1_cars.png")

        #create the Car
        car_rect = (150,90,70,125)
        car_img = self.car_ss.image_at(car_rect)

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
        self.speed=2
    def update(self):
        if self.angle_change != 0:
            self.direction.rotate_ip(self.angle_change)
            self.angle += self.angle_change
            # I prefer rotozoom because it looks smoother.
            self.image = pygame.transform.rotozoom(self.og_img, -self.angle, 1)
            self.rect = self.image.get_rect(center=self.rect.center)
        #update the positon vector and the rect
        self.position += self.direction * self.speed
        self.rect.center = self.position
    """
    def move
    def rotate
    def update
    """
    