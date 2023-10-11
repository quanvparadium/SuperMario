import sys

import os
import pygame

import pygame_menu
from constants import *

if __name__ == "__main__":
    #Init pygame
    pygame.init()

    #Game clock
    clock = pygame.time.Clock()

    #Create window
    surface = pygame.display.set_mode((W_WIDTH_SIZE, W_HEIGHT_SIZE))
    
    # Title and icon
    pygame.display.set_caption('Super Mario')
    # icon = pygame.image.load('Mario/assets/spaceship.png')
    # pygame.display.set_icon(icon)

    menu = pygame_menu.Menu('SUPER MARIO', W_WIDTH_SIZE, W_HEIGHT_SIZE,
                            onclose=None,
                            theme=CUSTOME_THEME,
                            mouse_motion_selection=True,)
    
    while True:
        deltatime = clock.tick(FPS)

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        try:
            menu.mainloop(surface)
        except:
            pass
            
        pygame.display.update()
    

