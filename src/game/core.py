import os
import pygame 
from pygame.locals import *

from constants import *
from game.readymenu import ReadyMenu
from game.loadingmenu import LoadingMenu
from game.map import Map
from components.sound import Sound


class Manager(object):
    """

    That class allows to easily handle game states. Depending on the situation,
    it updates and renders different things.

    """
    def __init__(self, core):

        self.currentGameState = 'LOADING'

        # self.oReadyMenu = ReadyMenu()
        print("READYMENU CHECKED")
        self.oLoadingMenu = LoadingMenu(core)

    def update(self, core):
        # print("CURRENT STATE UPDATING: ", self.currentGameState)
        if self.currentGameState == 'MENU':
            pass
            raise Exception("FAULT NOT EXIST MENU")

        elif self.currentGameState == 'LOADING':
            self.oLoadingMenu.update(core)

        elif self.currentGameState == 'INGAME':
            # core.get_map().update(core)
            pass

    def render(self, core):
        # print("CURRENT STATE RENDERING: ", self.currentGameState)
        if self.currentGameState == 'MENU':
            core.get_map().render_map(core)
            self.oReadyMenu.render(core)

        elif self.currentGameState == 'LOADING':
            print("RENDER LOADING ......................................")
            self.oLoadingMenu.render(core)

        elif self.currentGameState == 'INGAME':
            core.get_map().render(core)
            core.get_map().get_ui().render(core)
            pass

        # pygame.display.update()

    def start_loading(self):
            # Start to load the level
            self.currentGameState = 'LOADING'
            self.oLoadingMenu.update_time()


class Core(object):
    def __init__(self, surface, W_HEIGHT_SIZE, W_WIDTH_SIZE, id_map: str = '1-1'):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        
        self.screen = surface
        self.clock = pygame.time.Clock()
        
        self.oWorld = Map(id_map)
        self.oSound = Sound()
        print("CHECKING SOUND")
        self.oManager = Manager(self)

        self.run = True
        self.keyR = False
        self.keyL = False
        self.keyU = False
        self.keyD = False
        self.keyShift = False
        self.ESC  = False
        # print("CHECKING")
    
    def main_loop(self, events):
        self.input(events)
        self.update()
        self.render()
        self.clock.tick(FPS)

    def input(self, events):
        if self.get_manager().currentGameState == 'INGAME':
            self.input_player(events)
        else:
            self.input_menu(events)

    def input_menu(self, events):
        for e in events:
            if e.type == pygame.QUIT:
                self.run = False

            elif e.type == KEYDOWN:
                if e.key == K_RETURN:
                    self.get_manager().start_loading()            
    def input_player(self, events):
        for e in events:

            if e.type == pygame.QUIT:
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
                    # self.get_sound().stop()
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

    # GET ATTRIBUTE
    def get_manager(self):
        return self.oManager
    
    def get_sound(self):
        return self.oSound
    
    def get_map(self):
        return self.oWorld
    

    # UPDATE UI
    def update(self):
        # print("===========\nCORE UPDATING...")
        self.get_manager().update(self)

    def render(self):
        # print("===========\nCORE RENDERING...")
        self.get_manager().render(self)

    def should_quit(self):
        return self.ESC