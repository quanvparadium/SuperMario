import pygame
from pytmx.util_pygame import load_pygame

from constants import *
from components.player import Player
from components.platform import Platform
from components.camera import Camera
from components.bgobject import BGObject
# from components.coin import Coin
from game.background import BackgroundUI

class Map(object):
    def __init__(self, id_map):
        self.map = None
        self.obj = []
        self.obj_bg = []
        self.tubes = []
        self.debris = []
        self.mobs = []
        self.flag = None

        self.mapSize = (0, 0) #(width, height)
        self.sky = None

        self.id_map = id_map
        self.loadWorld()

        self.in_event = False
        self.tick = 0
        self.time = 400

        self.oPlayer = Player(x_pos=128, y_pos = 351)
        self.oCamera = Camera(self.mapSize[0] * 32, 14)
        self.oBackgroundUI = BackgroundUI()

    def loadWorld(self):
        print("LOADING WORLD .......")
        tmx_data = load_pygame(f"assets/worlds/{self.id_map}/W{self.id_map.replace('-', '')}.tmx")
        self.mapSize = (tmx_data.width, tmx_data.height)
        self.sky = pygame.Surface((W_WIDTH_SIZE, W_HEIGHT_SIZE))
        self.sky.fill((pygame.Color('#5c94fc')))

        # Initial map with zero-like array (width, height)
        self.map = [[0] * tmx_data.height for i in range(tmx_data.width)]
        print("BEGIN CHECKING WORLD")
        layer_num = 0
        print(tmx_data.visible_layers)
        print(tmx_data.images)
        for layer in tmx_data.visible_layers:
            # if layer.name == "Foreground":
            #     print("=====================================================================================")
            #     return
            for y in range(tmx_data.height):
                for x in range(tmx_data.width):

                    # Getting pygame surface
                    image = tmx_data.get_tile_image(x, y, layer_num)
                    

                    # It's none if there are no tile in that place
                    if image is not None:
                        # print("BEGIN GET TILE GID ...")
                        tileID = tmx_data.get_tile_gid(x, y, layer_num)
                        # print("BEGIN FOREGROUND")
                        if layer.name == 'Foreground':
                            # 22 ID is a question block, so in taht case we shoud load all it's images
                            if tileID == 22:
                                image = (
                                    image,                                      # 1
                                    tmx_data.get_tile_image(0, 15, layer_num),   # 2
                                    tmx_data.get_tile_image(1, 15, layer_num),   # 3
                                    tmx_data.get_tile_image(2, 15, layer_num)    # activated
                                )
                            # Map class has 1)"map" list, which is used in collision system because we can
                            # easily get block by x and y coordinate 2)"obj", "obj_bg" and simular arrays -
                            # they are used in rendering because you don't need to cycle through every
                            # (x, y) pair. Here we are adding the same platform object in 2 different arrays.
                            self.map[x][y] = Platform(x * tmx_data.tileheight, y * tmx_data.tilewidth, image, tileID)
                            print("TILE ID: ", tileID)
                            self.obj.append(self.map[x][y])   
                            # raise Exception("ERROROOROR")


                        elif layer.name == 'Background':
                            self.map[x][y] = BGObject(x * tmx_data.tileheight, y * tmx_data.tilewidth, image)
                            self.obj_bg.append(self.map[x][y])
                            # pass
                        else: 
                            raise Exception("ERROROOROR")

    def get_camera(self):
        return self.oCamera

    def get_name(self):
        return self.id_map

    def get_player(self):
        return self.oPlayer

    def get_ui(self):
        return self.oBackgroundUI


    def get_blocks_below(self, x, y):
        """
            Trả về hai giá trị dưới Entity để kiểm tra xem có nằm trên nền không (on_ground)
        """
        return (
            self.map[x][y + 1],
            self.map[x + 1][y + 1]
        )

    def update(self, core):
        # self.get_player().update(core)
        pass

    def render(self, core):
        core.screen.blit(self.sky, (0, 0))

        for obj in self.obj_bg:
            obj.render(core)    

        # for obj in self.obj:
        #     print("RENDERING OBJECT....", obj)
        #     obj.render(core)    

        self.get_player().render(core)

        self.get_ui().render(core)

        pass