import sys
import pygame
import pygame_menu
from pygame.locals import *

from constants import *
from game.core import Core


CURRENT_STATE = 'START_MENU'

class StartGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((W_WIDTH_SIZE, W_HEIGHT_SIZE))
        self.mainmenu = None
        self.playgame_menu = None
        self.option_menu = None
        self.about_menu = None
        self.running = True

    def _create_mainmenu(self):
        self.mainmenu = pygame_menu.Menu('SUPER MARIO', W_WIDTH_SIZE, W_HEIGHT_SIZE,
                            onclose=None,
                            theme=CUSTOME_THEME,
                            mouse_motion_selection=True,)
        self.mainmenu.add.button('PLAY GAME', self.playgame_menu)
        self.mainmenu.add.button('OPTION', self.option_menu)
        # self.mainmenu.add.button('ABOUT', self.about_menu)
        self.mainmenu.add.button('QUIT', pygame_menu.events.EXIT) 

    def _create_playgame_menu(self):
        self.playgame_menu = pygame_menu.Menu('SUPER MARIO', W_WIDTH_SIZE, W_HEIGHT_SIZE,
                            onclose=None,
                            theme=CUSTOME_THEME,
                            mouse_motion_selection=True,)
        
        def free_play_chosen_level(id_map: str):
            global GAME, CURRENT_STATE
            self.mainmenu.disable()
            GAME = Core(self.surface, W_HEIGHT_SIZE, W_WIDTH_SIZE, id_map)
            CURRENT_STATE = 'INGAME'

        self.free_play_menu = pygame_menu.Menu('CHOOSE LEVEL', W_WIDTH_SIZE, W_HEIGHT_SIZE,
                            onclose=None,
                            theme=CUSTOME_THEME,
                            mouse_motion_selection=True,)
        self.free_play_menu.add.button('WORLD 1 - 1', free_play_chosen_level, '1-1')

        self.playgame_menu.add.button('PLAY 1-1', self.free_play_menu)
        self.playgame_menu.add.button('BACK', pygame_menu.events.BACK)

    def _create_option_menu(self):
        self.option_menu = pygame_menu.Menu('SUPER MARIO', W_WIDTH_SIZE, W_HEIGHT_SIZE,
                            onclose=None,
                            theme=CUSTOME_THEME,
                            mouse_motion_selection=True,)
        self.option_menu.add.progress_bar("Sound: ", progressbar_id = "1", default=0, width = 150)
        


    def run(self):
        global CURRENT_STATE
        self._create_playgame_menu()
        self._create_option_menu()
        # self._create
        self._create_mainmenu()

        while self.running:
            events = pygame.event.get()

            if CURRENT_STATE == 'INGAME':
                GAME.main_loop(events)
                if GAME.should_quit():
                    CURRENT_STATE = 'START_MENU'
                    self.mainmenu.enable()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # elif event.type == KEYDOWN and event.key == K_SPACE:
                #     print("CHECKEDEDEDED")
                #     pygame.quit()
                #     sys.exit()                    

            try:
                self.mainmenu.mainloop(self.surface)
                print("COMBACK MAINLOOP")
            except:
                print("MAIN DISABLED", pygame.time.get_ticks())
                pass
            pygame.display.update()            