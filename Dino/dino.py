import pygame

class Dino:
    def __init__(self):
        self.img = pygame.image.load(r'C:\Users\movavi_school\Desktop\Khareboynik\img\dino.png')
        self.pos = [0, 375]

    def draw(self, screen):
        screen.blit(self.img, self.pos)