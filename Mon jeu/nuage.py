import pygame
import pytmx


class Nuage(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('nuage.png')
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]

        tmx_data = pytmx.util_pygame.load_pygame('carte_verti.tmx')
        nuage_position = tmx_data.get_object_by_name('Nuage1')
        nuage_position2 = tmx_data.get_object_by_name('Fin_nuage1')
        self.nuage = Nuage(nuage_position.x, nuage_position.y)

    def move_left(self):
        self.position[0] -= 1

    def get_image(self, x, y):
        nuage = pygame.Surface([128, 128])
        nuage.blit(self.sprite_sheet, (0, 0), (x, y, 128, 128))
        return nuage

    def deplacement(self): pass
