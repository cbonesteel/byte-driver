import pygame, sys
from .objs.car import Car
from .settings.options import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    #create the sprites and groups
    moving_sprites = pygame.sprite.Group()

    #create one car
    car1 = Car(100,100)
    moving_sprites.add(car1)

    while True:
        delta = clock.tick(60)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif(event.key == pygame.K_LEFT):
                        car1.angle_change = -3
                    elif event.key == pygame.K_RIGHT:
                        car1.angle_change = 3
                elif event.type == pygame.KEYUP:
                    # Stop rotating if the player releases the keys.
                    if event.key == pygame.K_RIGHT and car1.angle_change > 0:
                        car1.angle_change = 0
                    elif event.key == pygame.K_LEFT and car1.angle_change < 0:
                        car1.angle_change = 0

        screen.fill((0,0,0))
        moving_sprites.update()
        moving_sprites.draw(screen)
        pygame.display.update()