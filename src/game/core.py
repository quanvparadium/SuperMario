from os import environ

import pygame as pg
from pygame.locals import *

from constants import *
from game.map import Map
# from MenuManager import MenuManager
from components.sound import Sound

import pygame as pg

from game.loadingmenu import LoadingMenu
# from game.mainmenu import MainMenu



class MenuManager(object):
    """

    That class allows to easily handle game states. Depending on the situation,
    it updates and renders different things.

    """
    def __init__(self, core):

        self.currentGameState = 'Loading'

        # self.oMainMenu = MainMenu()
        self.oLoadingMenu = LoadingMenu(core)

    def update(self, core):
        if self.currentGameState == 'MainMenu':
            pass

        elif self.currentGameState == 'Loading':
            self.oLoadingMenu.update(core)

        elif self.currentGameState == 'Game':
            core.get_map().update(core)

    def render(self, core):
        if self.currentGameState == 'MainMenu':
            pass
            # core.get_map().render_map(core)
            # self.oMainMenu.render(core)

        if self.currentGameState == 'Loading':
            self.oLoadingMenu.render(core)

        elif self.currentGameState == 'Game':
            core.get_map().render(core)
            core.get_map().get_ui().render(core)

        pg.display.update()

    def start_loading(self):
            # Start to load the level
            self.currentGameState = 'Loading'
            self.oLoadingMenu.update_time()



class Core(object):
    """

    Main class.

    """
    def __init__(self, surface, W_HEIGHT_SIZE, WINDOW_H, id_map: str = '1-1', volume=0.5):
        environ['SDL_VIDEO_CENTERED'] = '1'
        # pg.mixer.pre_init(44100, -16, 2, 1024)
        # pg.init()
        # pg.display.set_caption('Mario by S&D')
        # pg.display.set_mode((W_HEIGHT_SIZE, WINDOW_H))

        # self.screen = pg.display.set_mode((W_HEIGHT_SIZE, WINDOW_H))
        self.screen = surface
        # print("====1====")
        self.clock = pg.time.Clock()
        # print("====2====")
        self.oWorld = Map(id_map)
        # print("====3====")
        self.oSound = Sound()
        # print("====4====")
        self.oMM = MenuManager(self)
        # print("OKIEIEIIEIEIEI")

        self.volume = volume

        self.run = True
        self.keyR = False
        self.keyL = False
        self.keyU = False
        self.keyD = False
        self.keyShift = False
        self.ESC = False

    def main_loop(self, events):
        # while self.run:
        # print(pg.time.get_ticks())
        self.input(events)
        self.update()
        self.render()
        self.clock.tick(FPS)

    def input(self, events):
        if self.get_mm().currentGameState == 'Game':
            self.input_player(events)
        else:
            self.input_menu(events)

    def input_player(self, events):
        for e in events:

            if e.type == pg.QUIT:
                self.run = False

            elif e.type == KEYDOWN:
                if e.key == K_RIGHT:
                    self.keyR = True
                elif e.key == K_LEFT:
                    self.keyL = True
                elif e.key == K_DOWN:
                    self.keyD = True
                elif e.key == K_UP:
                    self.keyU = True
                elif e.key == K_LSHIFT:
                    self.keyShift = True
                elif e.key == K_ESCAPE:
                    self.ESC = True
                    self.get_sound().stop('overworld')
                    self.get_sound().stop('overworld_fast')



            elif e.type == KEYUP:
                if e.key == K_RIGHT:
                    self.keyR = False
                elif e.key == K_LEFT:
                    self.keyL = False
                elif e.key == K_DOWN:
                    self.keyD = False
                elif e.key == K_UP:
                    self.keyU = False
                elif e.key == K_LSHIFT:
                    self.keyShift = False

    def input_menu(self, events):
        for e in events:
            if e.type == pg.QUIT:
                self.run = False

            elif e.type == KEYDOWN:
                if e.key == K_RETURN:
                    self.get_mm().start_loading()

    def update(self):
        self.get_mm().update(self)

    def render(self):
        self.get_mm().render(self)

    def get_map(self):
        return self.oWorld

    def get_mm(self):
        return self.oMM

    def get_sound(self):
        return self.oSound
    
    def get_volume(self):
        return self.volume

    def should_quit(self):
        return self.ESC