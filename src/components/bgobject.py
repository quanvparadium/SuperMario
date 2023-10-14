import pygame


class BGObject(object):
    def __init__(self, x, y, image):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.image = image
        self.type = 'BGObject'

    def render(self, core):
        core.screen.blit(self.image, core.get_map().get_camera().apply(self))
