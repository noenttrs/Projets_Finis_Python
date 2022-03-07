import threading
import time
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('player.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            'left': self.get_image(0, 0),
            'right': self.get_image(16, 0),

        }
        self.feet = pygame.Rect(0, 0, 16, 16)
        self.old_position = self.position.copy()
        self.speed = 2
        # self.vit_jump = 4

        # gestion des sauts

        self.a_jump = False
        self.montee = 0
        self.descente = 10
        self.saut = 0

    def save_location(self): self.old_position = self.position.copy()

    def change_animation(self, name):
        self.image.set_colorkey([0, 0, 0])
        self.image = self.images[name]

    def move_right(self): self.position[0] += self.speed

    def move_left(self): self.position[0] -= self.speed

    def jump(self):

        if self.a_jump:

            if self.montee >= 22:
                self.descente -= 1
                self.saut = self.descente

            else:
                self.montee += 1
                self.saut = self.montee

            if self.descente < 0:
                self.descente = 10
                self.montee = 0
                self.a_jump = False

            self.position[1] = self.position[1] - (self.saut/2)

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_up(self):
        def loop1_10():
            self.position[1] -= self.speed
            time.sleep(1)
            self.position[1] += self.speed

        threading.Thread(target=loop1_10).start()

    def go_start(self):
        self.position = [160, 6353]

    def get_image(self, x, y):
        image = pygame.Surface([16, 16])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16, 16))
        return image
