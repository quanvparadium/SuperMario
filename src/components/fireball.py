import pygame

from constants import *


class Fireball(object):
    def __init__(self, x_pos, y_pos, move_direction: bool):
        super().__init__()

        self.rect = pygame.Rect(x_pos, y_pos, 16, 16)
        self.state = 0
        self.direction = move_direction
        self.x_velocity = 5 if move_direction else -5
        self.y_velocity = 0

        self.current_image = 0
        self.image_tick = 0
        self.images = [pygame.image.load('assets/images/fireball.png').convert_alpha()]
        self.images.append(pygame.transform.flip(self.images[0], 0, 90))
        self.images.append(pygame.transform.flip(self.images[0], 90, 90))
        self.images.append(pygame.transform.flip(self.images[0], 90, 0))
        self.images.append(pygame.image.load('assets/images/firework0.png').convert_alpha())
        self.images.append(pygame.image.load('assets/images/firework1.png').convert_alpha())
        self.images.append(pygame.image.load('assets/images/firework2.png').convert_alpha())

    def update_image(self, core):
        self.image_tick += 1

        if self.state == 0:
            if self.image_tick % 15 == 0:
                self.current_image += 1
                if self.current_image > 3:
                    self.current_image = 0
                    self.image_tick = 0

        elif self.state == -1:
            if self.image_tick % 10 == 0:
                self.current_image += 1
            if self.current_image == 7:
                core.get_map().remove_whizbang(self)

    def start_boom(self):
        self.x_velocity = 0
        self.y_velocity = 0
        self.current_image = 4
        self.image_tick = 0
        self.state = -1

    def update_x_pos(self, blocks):
        self.rect.x += self.x_velocity
      
        for block in blocks:
            if block != 0 and block.type != 'BGObject':
                if pygame.Rect.colliderect(self.rect, block.rect):

                    # Fireball blows up only when collides on x-axis
                    self.start_boom()

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
        self.update_y_pos(blocks)
        self.update_x_pos(blocks)

        self.check_map_borders(core)

    def check_collision_with_mobs(self, core):
        for mob in core.get_map().get_mobs():
            if self.rect.colliderect(mob.rect):
                if mob.collision:
                    mob.die(core, instantly=False, crushed=False)
                    self.start_boom()

    def update(self, core):
        if self.state == 0:
            self.update_image(core)
            self.move(core)
            self.check_collision_with_mobs(core)
        elif self.state == -1:
            self.update_image(core)

    def render(self, core):
        core.screen.blit(self.images[self.current_image], core.get_map().get_camera().apply(self))
