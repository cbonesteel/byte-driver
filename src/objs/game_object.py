import pygame
from pygame.math import Vector2

class GameObject(pygame.sprite.Sprite):
    def __init__(self, pos, dimensions, angle=0, scale=1, color=(128, 128, 128), image=None):
        """pos: Vector2, dimensions: Vector2, angle: float, scale: float, color: tuple, image:pygame.Surface"""
        super(GameObject, self).__init__()

        self.pos = pos
        self.dimensions = dimensions
        self.angle = angle
        self.scale = scale
        self.color = color

        if image:
            self.surface = image
        else:
            self.surface = pygame.Surface((dimensions.x, dimensions.y), pygame.SRCALPHA)
            self.surface.fill(self.color)
        self.update_internal()

    def update_surface(self, surface, update_dimensions=False):
        """Used for updating the GameObject image."""
        self.surface = surface
        if update_dimensions:
            self.dimensions = Vector2(surface.get_size()[0], surface.get_size()[1])
        self.update_internal()

    def update_internal(self):
        self.image = pygame.transform.scale(self.surface, (self.dimensions.x * self.scale, self.dimensions.y * self.scale))
        self.image = pygame.transform.rotate(self.surface, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos.x, self.pos.y)
        self.mask = pygame.mask.from_surface(self.image)

    def rotate(self, angle):
        self.angle = (self.angle + angle) % 360
        self.update_internal()

    def set_pos(self, pos):
        self.pos.x = pos.x
        self.pos.y = pos.y
        self.update_internal()

    def move(self, pos):
        self.pos += pos
        self.update_internal()

    def is_colliding(self, other):
        return pygame.sprite.spritecollide(self, other, False, pygame.sprite.collide_mask)

    def update(self, deltaTime):
        pass

if __name__ == '__main__':
    pygame.init()
    SCREEN = WIDTH, HEIGHT = 288, 512
    win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)

    clock = pygame.time.Clock()
    FPS = 60
    count = 0

    moving_object = GameObject(Vector2(40, 40), Vector2(25, 25), 45)
    static_objects = [
        GameObject(Vector2(WIDTH // 2, HEIGHT // 3), Vector2(25, 25), 30),
        GameObject(Vector2(WIDTH // 4, HEIGHT // 2), Vector2(50, 25), 30),
        GameObject(Vector2(WIDTH * 3 // 4, HEIGHT * 2 // 3), Vector2(25, 25), 30)
    ]

    all_objs = pygame.sprite.Group([moving_object] + static_objects)
    static_objs = pygame.sprite.Group(static_objects)

    running = True
    while running:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        count += 1
        if count % 100 == 0:
            moving_object.rotate(10)
            count = 0
        pos = pygame.mouse.get_pos()
        moving_object.set_pos(Vector2(pos[0], pos[1]))

        collide = moving_object.is_colliding(static_objs)

        win.fill((255, 0, 0) if collide else (255,255,255))
        all_objs.update(dt)
        all_objs.draw(win)
        pygame.display.update()
    pygame.quit()
