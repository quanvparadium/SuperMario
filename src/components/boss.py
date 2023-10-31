import pygame

from components.Entity import Entity
from constants import *

class Boss(Entity):
    def __init__(self, x_pos, y_pos, move_direction):
        super().__init__()
        self.rect = pygame.Rect(x_pos, y_pos, 32, 32)

        if move_direction:
            self.x_velocity = 1
        else:
            self.x_velocity = -1

        self.crushed = False

        self.current_image = 0
        self.image_tick = 0
        self.images = [
            pygame.image.load('assets/images/Bowser/bowser_0.png').convert_alpha(),
            pygame.image.load('assets/images/Bowser/bowser_1.png').convert_alpha(),
            pygame.image.load('assets/images/Bowser/bowser_2.png').convert_alpha(),
            pygame.image.load('assets/images/Bowser/bowser_3.png').convert_alpha(),
        ]
        self.images.append(pygame.transform.flip(self.images[0], 0, 180))

        self.fire_timer = 0

        self.heart = 3
        

    def update_image(self):
        self.image_tick += 1
        if self.image_tick % 15 == 0:
            self.current_image += 1
        if self.current_image > 3:
            self.current_image = 0
            self.image_tick = 0

    def check_collision_with_player(self, core):
        if self.collision:
            if self.rect.colliderect(core.get_map().get_player().rect):
                if self.state != -1:
                    if not core.get_map().get_player().unkillable:
                        core.get_map().get_player().set_powerlvl(0, core)

    def check_collision_with_mobs(self, core):
        pass

    def update(self, core):
        if self.state == 0:
            self.update_image()

            if not self.on_ground:
                self.y_velocity += GRAVITY

            blocks = core.get_map().get_blocks_for_collision(int(self.rect.x // 32), int(self.rect.y // 32))
            self.update_x_pos(blocks)
            self.update_y_pos(blocks)

            self.check_map_borders(core)

        elif self.state == -1:
            if self.crushed:
                self.image_tick += 1
                if self.image_tick == 50:
                    core.get_map().get_mobs().remove(self)
            else:
                self.y_velocity += GRAVITY
                self.rect.y += self.y_velocity
                self.check_map_borders(core)

        if pygame.time.get_ticks() - self.fire_timer >= 2000:
            self.fire_timer = pygame.time.get_ticks()
            core.get_map().spawn_flame(self.rect.x, self.rect.y, self.x_velocity > 0)


    def render(self, core):
        if self.x_velocity > 0:
            core.screen.blit(pygame.transform.flip(self.images[self.current_image], True, False), core.get_map().get_camera().apply(self))
        else:
            core.screen.blit(self.images[self.current_image], core.get_map().get_camera().apply(self))

    def die(self, core, instantly, crushed):
        self.heart -= 1
        if (self.heart <= 0):
            core.get_map().get_mobs().remove(self)
            