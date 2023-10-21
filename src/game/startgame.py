# import sys
# import pygame
# import pygame_menu
# from pygame.locals import *

# from constants import *
# from game.core import Core


# CURRENT_STATE = 'START_MENU'

# class StartGame:
#     def __init__(self):
#         pygame.init()
#         self.clock = pygame.time.Clock()
#         self.surface = pygame.display.set_mode((W_WIDTH_SIZE, W_HEIGHT_SIZE))
#         self.mainmenu = None
#         self.playgame_menu = None
#         self.option_menu = None
#         self.about_menu = None
#         self.running = True

#     def _create_mainmenu(self):
#         self.mainmenu = pygame_menu.Menu('SUPER MARIO', W_WIDTH_SIZE, W_HEIGHT_SIZE,
#                             onclose=None,
#                             theme=CUSTOME_THEME,
#                             mouse_motion_selection=True,)
#         self.mainmenu.add.button('PLAY GAME', self.playgame_menu)
#         self.mainmenu.add.button('OPTION', self.option_menu)
#         # self.mainmenu.add.button('ABOUT', self.about_menu)
#         self.mainmenu.add.button('QUIT', pygame_menu.events.EXIT) 

#     def _create_playgame_menu(self):
#         self.playgame_menu = pygame_menu.Menu('SUPER MARIO', W_WIDTH_SIZE, W_HEIGHT_SIZE,
#                             onclose=None,
#                             theme=CUSTOME_THEME,
#                             mouse_motion_selection=True,)
        
#         def free_play_chosen_level(id_map: str):
#             global GAME, CURRENT_STATE
#             self.mainmenu.disable()
#             GAME = Core(self.surface, W_HEIGHT_SIZE, W_WIDTH_SIZE, id_map)
#             CURRENT_STATE = 'INGAME'

#         self.self.free_play_menu = pygame_menu.Menu('CHOOSE LEVEL', W_WIDTH_SIZE, W_HEIGHT_SIZE,
#                             onclose=None,
#                             theme=CUSTOME_THEME,
#                             mouse_motion_selection=True,)
#         self.self.free_play_menu.add.button('WORLD 1 - 1', free_play_chosen_level, '1-1')

#         self.playgame_menu.add.button('PLAY 1-1', self.self.free_play_menu)
#         self.playgame_menu.add.button('BACK', pygame_menu.events.BACK)

#     def _create_option_menu(self):
#         self.option_menu = pygame_menu.Menu('SUPER MARIO', W_WIDTH_SIZE, W_HEIGHT_SIZE,
#                             onclose=None,
#                             theme=CUSTOME_THEME,
#                             mouse_motion_selection=True,)
#         self.option_menu.add.progress_bar("Sound: ", progressbar_id = "1", default=0, width = 150)
        


#     def run(self):
#         global CURRENT_STATE
#         self._create_playgame_menu()
#         self._create_option_menu()
#         # self._create
#         self._create_mainmenu()

#         while self.running:
#             events = pygame.event.get()

#             if CURRENT_STATE == 'INGAME':
#                 GAME.main_loop(events)
#                 if GAME.should_quit():
#                     CURRENT_STATE = 'START_MENU'
#                     self.mainmenu.enable()

#             for event in events:
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 # elif event.type == KEYDOWN and event.key == K_SPACE:
#                 #     print("CHECKEDEDEDED")
#                 #     pygame.quit()
#                 #     sys.exit()                    

#             try:
#                 self.mainmenu.mainloop(self.surface)
#                 print("COMBACK MAINLOOP")
#             except:
#                 # print("MAIN DISABLED", pygame.time.get_ticks())
#                 pass
#             pygame.display.update()            

import sys
import pygame
import pygame_menu
from pygame.locals import *

from constants import *
from game.core import Core
import math

CURRENT_STATE = 'START_MENU'
NUMBER_OF_LEVELS = 32
LEVEL_PER_ROW = 8
DARK_BLUE = (0,0,139)
FONT_BOLD = pygame_menu.font.FONT_OPEN_SANS_BOLD

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

    def free_play_chosen_level(self, id_map: str):
        global GAME, CURRENT_STATE
        self.mainmenu.disable()
        GAME = Core(self.surface, W_HEIGHT_SIZE, W_WIDTH_SIZE, id_map)
        CURRENT_STATE = 'INGAME'

    def index_to_level(self, index):
        big_level = (index + 1 ) // 4
        small_level = (index + 1) % 4
        if small_level == 0:
            return f'{big_level}-{small_level+4}'
        else:
            return f'{big_level+1}-{small_level}'

    def level_chosen_btn_effect(is_select,widget):
        if is_select:
            widget.set_font(font_size=32,color='white',
                        font=FONT_BOLD,
                        background_color=DARK_BLUE,readonly_color=LIGHT_BLUE,
                        readonly_selected_color='white',selected_color='red',)
        else:
            widget.set_font(font_size=32,color='white',
                        font=FONT_BOLD,
                        background_color=LIGHT_BLUE,readonly_color=LIGHT_BLUE,
                        readonly_selected_color='white',selected_color='red',)

    def _create_playgame_menu(self):
        self.playgame_menu = pygame_menu.Menu('SUPER MARIO', W_WIDTH_SIZE, W_HEIGHT_SIZE,
                            onclose=None,
                            theme=CUSTOME_THEME,
                            mouse_motion_selection=True,)
        

        self.free_play_menu = pygame_menu.Menu('CHOOSE LEVEL', W_WIDTH_SIZE, W_HEIGHT_SIZE,
                            onclose=None,
                            theme=CUSTOME_THEME,
                            mouse_motion_selection=True,)
        self.free_play_menu.add.button('WORLD 1 - 1', self.free_play_chosen_level, '1-1')
        self.free_play_menu.add.label('LEVELS',font_size=40)

        # create level table structure
        for r_id in range(math.ceil(NUMBER_OF_LEVELS/LEVEL_PER_ROW)):
            f = self.free_play_menu.add.frame_h( W_WIDTH_SIZE, 60, margin=(0,0))

            for level_id in range(r_id*LEVEL_PER_ROW,
            min((r_id+1)*LEVEL_PER_ROW,NUMBER_OF_LEVELS)):
                btn = self.free_play_menu.add.button(f' {self.index_to_level(level_id)} ',
                                                self.free_play_chosen_level,
                                                self.index_to_level(level_id))
                btn.set_margin(0, 0)
                btn.set_padding((4,8))
                btn.set_selection_effect(pygame_menu.widgets.NoneSelection())
                # btn.set_selection_callback(self.level_chosen_btn_effect)

                f.pack(btn,align='align-center')


        self.playgame_menu.add.button('PLAY 1-1', self.free_play_menu)
        self.playgame_menu.add.button('BACK', pygame_menu.events.BACK)

    def _create_option_menu(self):
        self.option_menu = pygame_menu.Menu('SUPER MARIO', W_WIDTH_SIZE, W_HEIGHT_SIZE,
                            onclose=None,
                            theme=CUSTOME_THEME,
                            mouse_motion_selection=True,)
        self.option_menu.add.progress_bar("Sound: ", progressbar_id = "1", default=0, width = 150)


    def run(self):
        global CURRENT_STATE, GAME
        self._create_playgame_menu()
        self._create_option_menu()
        # self._create
        self._create_mainmenu()
        while self.running:
            # print("BEFORE RUNNING")
            events = pygame.event.get()
            # print(CURRENT_STATE)
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
                # print("MAIN DISABLED", pygame.time.get_ticks())
                pass
            pygame.display.update()