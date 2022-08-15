import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption('Valley')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        # check if we are closing the game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                dt = self.clock.tick(40) / 1000
                self.level.run(dt)
                pygame.display.update()

# check if we are in main file
if __name__ == '__main__':
    # creating object from class
    game = Game()
    # call run method
    game.run()
