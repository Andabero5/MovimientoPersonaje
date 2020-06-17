import pygame


class MySpriteAdapter(pygame.sprite.Sprite):

    def __init__(self, action):
        super(MySpriteAdapter, self).__init__()
        self.images = action
        self.index = 0
        self.rect = pygame.Rect(40, 40, 800, 600)

    def update(self):
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.index += 1
