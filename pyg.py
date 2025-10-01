import pygame
class UI:
    def __init__(self) -> None:
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
    def run(self):
        pygame.init()
        run = True
        while run:

            pygame.draw.rect(self.screen, (100, 100, 100), self.shape("s"))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()
        pygame.quit()
    def shape(self, shape):
        re = pygame.Rect((0,0,100,100))
        return re
ui = UI()
ui.run()