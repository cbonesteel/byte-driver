import pygame, sys
from .objs.car import Car
from .objs.camera import Camera
from .settings.options import *
from .objs.BitMap import BitMap

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    #background
    bitmap = BitMap(3,5)
    background = bitmap.getfinalimage()
    #background = pygame.image.load("./src/imgs/background.png")

    #create the sprites and groups
    camera_group = Camera(screen, background)

    #create one car
    car1 = Car(100,100,0)
    camera_group.add(car1)

    while True:
        delta = clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif(event.key == pygame.K_LEFT):
                    car1.angle_change = -5
                elif event.key == pygame.K_RIGHT:
                    car1.angle_change = 5
                elif event.key == pygame.K_UP:
                    car1.accel = True
                elif event.key == pygame.K_DOWN:
                    car1.brake = True
            elif event.type == pygame.KEYUP:
                # Stop rotating if the player releases the keys.
                if event.key == pygame.K_RIGHT and car1.angle_change > 0:
                    car1.angle_change = 0
                elif event.key == pygame.K_LEFT and car1.angle_change < 0:
                    car1.angle_change = 0
                elif event.key == pygame.K_UP:
                    car1.accel = False
                elif event.key == pygame.K_DOWN:
                    car1.brake = False

        screen.fill((0,0,0))
        camera_group.update(delta/1000)
        camera_group.camera_draw(car1)
        pygame.display.update()