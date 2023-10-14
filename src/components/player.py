import pygame 

class Player(object):
    def __init__(self, x_pos, y_pos):
        self.numOfLives = 3
        self.score = 0
        self.coins = 0

        self.visible = True
        self.spriteTick = 0
        self.powerLVL = 0

        self.unkillable = False
        self.unkillableTime = 0

        self.inLevelUpAnimation = False
        self.inLevelUpAnimationTime = 0
        self.inLevelDownAnimation = False
        self.inLevelDownAnimationTime = 0

        self.already_jumped = False
        self.next_jump_time = 0
        self.next_fireball_time = 0

        self.x_velocity = 0
        self.y_velocity = 0
        self.direction = True
        self.on_ground = False
        self.fast_moving = False

        self.pos_x = x_pos
        self.image = pygame.image.load('assets/images/mario/mario.png').convert_alpha()
        self.sprites = []
        # self.load_sprites()

        self.rect = pygame.Rect(x_pos, y_pos, 32, 32)
    
    def load_sprites(self):
        self.sprites = [
            # 0 Small, stay
            pygame.image.load('assets/images/Mario/mario.png'),

            # 1 Small, move 0
            pygame.image.load('assets/images/Mario/mario_move0.png'),

            # 2 Small, move 1
            pygame.image.load('assets/images/Mario/mario_move1.png'),

            # 3 Small, move 2
            pygame.image.load('assets/images/Mario/mario_move2.png'),

            # 4 Small, jump
            pygame.image.load('assets/images/Mario/mario_jump.png'),

            # 5 Small, end 0
            pygame.image.load('assets/images/Mario/mario_end.png'),

            # 6 Small, end 1
            pygame.image.load('assets/images/Mario/mario_end1.png'),

            # 7 Small, stop
            pygame.image.load('assets/images/Mario/mario_st.png'),

            # =============================================

            # 8 Big, stay
            pygame.image.load('assets/images/Mario/mario1.png'),

            # 9 Big, move 0
            pygame.image.load('assets/images/Mario/mario1_move0.png'),

            # 10 Big, move 1
            pygame.image.load('assets/images/Mario/mario1_move1.png'),

            # 11 Big, move 2
            pygame.image.load('assets/images/Mario/mario1_move2.png'),

            # 12 Big, jump
            pygame.image.load('assets/images/Mario/mario1_jump.png'),

            # 13 Big, end 0
            pygame.image.load('assets/images/Mario/mario1_end.png'),

            # 14 Big, end 1
            pygame.image.load('assets/images/Mario/mario1_end1.png'),

            # 15 Big, stop
            pygame.image.load('assets/images/Mario/mario1_st.png'),

            # =============================================

            # 16 Big_fireball, stay
            pygame.image.load('assets/images/Mario/mario2.png'),

            # 17 Big_fireball, move 0
            pygame.image.load('assets/images/Mario/mario2_move0.png'),

            # 18 Big_fireball, move 1
            pygame.image.load('assets/images/Mario/mario2_move1.png'),

            # 19 Big_fireball, move 2
            pygame.image.load('assets/images/Mario/mario2_move2.png'),

            # 20 Big_fireball, jump
            pygame.image.load('assets/images/Mario/mario2_jump.png'),

            # 21 Big_fireball, end 0
            pygame.image.load('assets/images/Mario/mario2_end.png'),

            # 22 Big_fireball, end 1
            pygame.image.load('assets/images/Mario/mario2_end1.png'),

            # 23 Big_fireball, stop
            pygame.image.load('assets/images/Mario/mario2_st.png'),
        ]

        # Left side
        for i in range(len(self.sprites)):
            self.sprites.append(pygame.transform.flip(self.sprites[i], 180, 0))

        # Power level changing, right
        self.sprites.append(pygame.image.load('assets/images/Mario/mario_lvlup.png').convert_alpha())

        # Power level changing, left
        self.sprites.append(pygame.transform.flip(self.sprites[-1], 180, 0))

        # Death
        self.sprites.append(pygame.image.load('assets/images/Mario/mario_death.png').convert_alpha())

    def update(self, core):
        # self.player_physics(core)
        print("WILL UPDATING PLAYER AFTER")
        pass

    def render(self, core):
        # print("WILL RENDERING PLAYER AFTER .......")
        if self.visible:
            core.screen.blit(self.image, core.get_map().get_camera().apply(self))
    
    