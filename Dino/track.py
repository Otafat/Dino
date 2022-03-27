import pygame

class Track:
    def __init__(self):
        self.img = pygame.image.load(r'C:\Users\movavi_school\Desktop\Khareboynik\img\track.png')
        self.poses = []
        self.create()

    def create(self):
        self.poses.append([0, 450])
        self.poses.append([1200, 450])

    def move(self):
        for pos in self.poses:
            pos[0] -= 0.125
            if pos[0] < -1200:
                pos[0] = 1199

    def draw(self, screen):
        for i in self.poses:
            screen.blit(self.img, i)
