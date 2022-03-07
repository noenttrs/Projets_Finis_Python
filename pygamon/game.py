import pygame
import pytmx
import pyscroll

from player import Player


class Game:
    def __init__(self):
        # créer la fenêtre de jeu
        self.screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("Pygamon - Aventure")

        # charger la carte(tmx)
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # générer un joueur
        player_position = tmx_data.get_object_by_name('Player')
        self.player = Player(player_position.x, player_position.y)

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de carte
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        enter_house = tmx_data.get_object_by_name('enter_house')
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        enter_house2 = tmx_data.get_object_by_name('enter_house2')
        self.enter_house_rect2 = pygame.Rect(enter_house2.x, enter_house2.y, enter_house2.width, enter_house2.height)

        enter_house3 = tmx_data.get_object_by_name('enter_house3')
        self.enter_house_rect2 = pygame.Rect(enter_house3.x, enter_house3.y, enter_house3.width, enter_house3.height)

        self.map = 'world'

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        if pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')

    def switch_house(self):
        # charger la carte(tmx)
        tmx_data = pytmx.util_pygame.load_pygame('house.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de carte
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        enter_house = tmx_data.get_object_by_name('exit_house')
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        spawn_house_point = tmx_data.get_object_by_name('spawn_house')
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y - 20

    def switch_world(self):
        # charger la carte(tmx)
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de carte
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        enter_house = tmx_data.get_object_by_name('enter_house')
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        exit_house_point = tmx_data.get_object_by_name('exit_house_point')
        self.player.position[0] = exit_house_point.x
        self.player.position[1] = exit_house_point.y

    def switch_house2(self):
        # charger la carte(tmx)
        tmx_data = pytmx.util_pygame.load_pygame('house.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de carte
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        enter_house = tmx_data.get_object_by_name('exit_house')
        self.enter_house_rect2 = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        spawn_house_point = tmx_data.get_object_by_name('spawn_house')
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y - 20

    def switch_world2(self):
        # charger la carte(tmx)
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de carte
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        enter_house = tmx_data.get_object_by_name('enter_house2')
        self.enter_house_rect2 = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        exit_house_point = tmx_data.get_object_by_name('exit_house_point2')
        self.player.position[0] = exit_house_point.x
        self.player.position[1] = exit_house_point.y

    def update(self):
        self.group.update()

        if self.map == 'world' and self.player.feet.colliderect(self.enter_house_rect):
            self.switch_house()
            self.map = 'house'

        if self.map == 'house' and self.player.feet.colliderect(self.enter_house_rect):
            self.switch_world()
            self.map = 'world'

        if self.map == 'world' and self.player.feet.colliderect(self.enter_house_rect2):
            self.switch_house2()
            self.map = 'house'

        if self.map == 'house' and self.player.feet.colliderect(self.enter_house_rect2):
            self.switch_world2()
            self.map = 'world'

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):

        clock = pygame.time.Clock()

        running = True
        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)
        pygame.quit()
