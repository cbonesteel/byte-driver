import pygame, sys
from .car import Car
from .settings.options import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    #create the sprites and groups
    moving_sprites = pygame.sprite.Group()
    car1 = Car(100,100)
    moving_sprites.add(car1)

    while True:
        delta = clock.tick(60)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        moving_sprites.draw(screen)
        pygame.display.update()