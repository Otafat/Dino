import pygame
import sys
from pygame.color import THECOLORS

from dino import Dino
from track import Track

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 500))
        self.dino = Dino()
        self.track = Track()

    def draw(self):
        self.screen.fill(THECOLORS['white'])
        self.dino.draw(self.screen)
        self.track.draw(self.screen)

    def get_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def start(self):
        while True:
            self.get_keys()
            self.draw()
            self.track.move()
            pygame.display.flip()
main = Main()
main.start()