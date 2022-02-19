import pygame 

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
        image = pygame.Surface(rect.size).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey = None):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect, colorkey) for rect in rects]

    """
    offset here is a horizontal offset
    """
    def load_strip(self, rect, image_count, offset=0, colorkey = None):
        """Load a whole strip of images, and return them as a list."""
        tups = []
        for x in range(image_count):
            if(x == 0):
                tups.append((rect[0]+rect[2]*x, rect[1], rect[2], rect[3]))
            else:
                tups.append((rect[0]+(rect[2]+offset)*x, rect[1], rect[2], rect[3]))
        return self.images_at(tups, colorkey)