import pygame
from constants import * 
from components.text import Text

class ReadyMenu(object):
    def __init__(self):
        print("INITING READYMENU")
        self.mainImage = pygame.image.load(r'assets/images/super_mario_bros.png').convert_alpha()

        self.toStartText = Text('Press ENTER to start', 16, (W_WIDTH_SIZE - W_WIDTH_SIZE * 0.72, W_HEIGHT_SIZE - W_HEIGHT_SIZE * 0.3))

    def render(self, core):
        core.screen.blit(self.mainImage, (50, 50))
        self.toStartText.render(core)
