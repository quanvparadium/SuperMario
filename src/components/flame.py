import pygame

from constants import *


class Flame(object):
    def __init__(self, x_pos, y_pos, move_direction: bool):
        super().__init__()

        self.rect = pygame.Rect(x_pos, y_pos, 16, 16)
        self.state = 0
        self.direction = move_direction
        self.x_velocity = 5 if move_direction else -5
        self.y_velocity = 0

        self.current_image = 0
        self.image_tick = 0
        self.images = [
            pygame.image.load('assets/images/flame_0.png').convert_alpha(),
            pygame.image.load('assets/images/flame_1.png').convert_alpha(),
        ]
        self.images.append(pygame.transform.flip(self.images[0], 0, 180))
        
        self.collision = True

    def update_image(self, core):
        self.image_tick += 1
        if self.image_tick == 14:
            self.current_image = 1
        elif self.image_tick == 28:
            self.current_image = 0
            self.image_tick = 0

    def start_boom(self, core):
        self.x_velocity = 0
        self.y_velocity = 0
        self.image_tick = 0
        self.state = -1
        core.get_map().remove_whizbang(self)

    def update_x_pos(self, blocks, core):
        self.rect.x += self.x_velocity
      
        for block in blocks:
            if block != 0 and block.type != 'BGObject':
                if pygame.Rect.colliderect(self.rect, block.rect):

                    # Fireball blows up only when collides on x-axis
                    self.start_boom(core)

    def update_y_pos(self, blocks):
        self.rect.y += self.y_velocity
        for block in blocks:
            if block != 0 and block.type != 'BGObject':
                if pygame.Rect.colliderect(self.rect, block.rect):
                    self.rect.bottom = block.rect.top
                    self.y_velocity = -3

    def check_map_borders(self, core):
        if self.rect.x <= 0:
            core.get_map().remove_whizbang(self)
        elif self.rect.x >= 6768:
            core.get_map().remove_whizbang(self)
        elif self.rect.y > 448:
            core.get_map().remove_whizbang(self)

    def move(self, core):
        self.y_velocity += GRAVITY

        blocks = core.get_map().get_blocks_for_collision(self.rect.x // 32, self.rect.y // 32)
        # self.update_y_pos(blocks)
        self.update_x_pos(blocks, core)

        self.check_map_borders(core)

    def check_collision_with_player(self, core):
        if self.collision:
            if self.rect.colliderect(core.get_map().get_player().rect):
                if not core.get_map().get_player().unkillable:
                    self.collision = False
                    core.get_map().get_player().set_powerlvl(0, core)

    def update(self, core):
        if self.state == 0:
            self.update_image(core)
            self.move(core)
            self.check_collision_with_player(core)
        elif self.state == -1:
            self.update_image(core)

    def render(self, core):
        if self.x_velocity > 0:
            core.screen.blit(pygame.transform.flip(self.images[self.current_image], True, False), core.get_map().get_camera().apply(self))
        else:
            core.screen.blit(self.images[self.current_image], core.get_map().get_camera().apply(self))
