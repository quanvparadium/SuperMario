import pygame as pygame

class Text(object):
    def __init__(self, text, fontsize, rectcenter, font='Emulogic', textcolor = (255, 255, 255)):
        self.font = pygame.font.Font('assets/fonts/emulogic.ttf', fontsize)
        self.text = self.font.render(text, False, textcolor)
        self.rect = self.text.get_rect(center=rectcenter)
        self.y_offset = 0

    def update(self, core):
        self.rect.y -= 1
        self.y_offset -= 1

        # Sẽ xoá trong 100 tictak
        if self.y_offset == -100:
            core.get_map().remove_text(self)

    def render(self, core):
        core.screen.blit(self.text, self.rect)

    def render_in_game(self, core):
        core.screen.blit(self.text, core.get_map().get_camera().apply(self))
