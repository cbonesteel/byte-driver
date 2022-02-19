import pygame
import pygments
from ..settings.options import WINDOW_HEIGHT, WINDOW_WIDTH
from pygame.math import Vector2

class Camera(pygame.sprite.Group):
    """
    Track for now will be an image. Once multiple tracks are added, change this to track.background or whatever
    """
    def __init__(self, surface, track):
        super().__init__()
        self.display_surface = surface

        # camera offset
        self.offset = pygame.math.Vector2()

        # ground
        self.ground_surf = track
        self.ground_rect = self.ground_surf.get_rect(topleft=(0,0))

    def center_target(self, target):
        self.offset.x = target.rect.centerx - (WINDOW_WIDTH / 2)
        self.offset.y = target.rect.centery - (WINDOW_HEIGHT / 2)

    def camera_draw(self, player):
        self.center_target(player)

        # ground
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf, ground_offset)

        # active elements
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
