import pygame
from constants import *
from components.text import Text


class LoadingMenu(object):
    def __init__(self, core):
        self.iTime = pygame.time.get_ticks()
        self.loadingType = True
        self.bg = pygame.Surface((W_WIDTH_SIZE, W_HEIGHT_SIZE))
        self.text = Text('WORLD 1-1', 32, (W_WIDTH_SIZE / 2, W_HEIGHT_SIZE / 2))
        print("INITED LOADINGMENU")

    def update(self, core):
        if pygame.time.get_ticks() >= self.iTime + (5250 if not self.loadingType else 2500):
            if self.loadingType:
                core.oManager.currentGameState = 'INGAME'
                core.get_sound().play('overworld', 999999, 0.5)
                print("PLAYING OVERWORLD")
                core.get_map().in_event = False
            else:
                core.oManager.currentGameState = 'READYMENU'
                self.set_text_and_type('WORLD 1-1', True)
                core.get_map().reset(True)

    def set_text_and_type(self, text, type):
        self.text = Text(text, 32, (W_WIDTH_SIZE / 2, W_HEIGHT_SIZE / 2))
        self.loadingType = type

    def render(self, core):
        core.screen.blit(self.bg, (0, 0))
        self.text.render(core)

    def update_time(self):
        self.iTime = pygame.time.get_ticks()
