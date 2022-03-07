import pygame


class Menu:

    def __init__(self):
        self.screen = pygame.display.set_mode((720, 720))
        pygame.display.set_caption("Nono - Aventure")



    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
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

