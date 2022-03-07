import pygame
import pyscroll
import pytmx

# import time
from player import Player


# from nuage import Nuage


class Game:

    def __init__(self):
        self.good = False
        self.value_gravity = 3
        self.screen = pygame.display.set_mode((544, 720))
        pygame.display.set_caption("Nono - Aventure")
        pygame.mixer.music.load('music.wav')

        # charger la carte(tmx)
        tmx_data = pytmx.util_pygame.load_pygame('carte_verti.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2.5

        self.collision = []
        self.walls = []
        '''self.void = []'''
        self.floor = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.collision.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        for obj in tmx_data.objects:
            if obj.type == "walls":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        for floor in tmx_data.objects:
            if floor.type == "floor":
                self.floor.append(pygame.Rect(floor.x, floor.y, floor.width, floor.height))

        player_position = tmx_data.get_object_by_name('Player')
        self.player = Player(player_position.x, player_position.y)

        # nuage_position = tmx_data.get_object_by_name('Nuage1')
        # self.nuage = Nuage(nuage_position.x, nuage_position.y)

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('right')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('left')

        if pressed[pygame.K_SPACE] and self.player.a_jump == False and self.good:
            self.player.a_jump = True
            # self.player.move_up()

    def launch_music(self):
        pygame.mixer.music.play()

    def gravity(self):
        self.player.position[1] += 3

    def update(self):
        self.group.update()

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()
                sprite.move_back()

            if sprite.feet.collidelist(self.collision) > -1:
                self.good = True

            elif sprite.feet.collidelist(self.floor) > -1:
                self.good = True

            else:
                self.good = False
                self.gravity()

    def run(self):

        clock = pygame.time.Clock()

        self.launch_music()

        running = True
        while running:

            pressed = pygame.key.get_pressed()
            self.player.save_location()
            self.handle_input()
            self.update()
            self.player.jump()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if pressed[pygame.K_ESCAPE]:
                    running = False
            clock.tick(60)
        pygame.quit()

