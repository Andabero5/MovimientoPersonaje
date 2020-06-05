import pygame
import glob
from Logic.GoldenKnight import *
from Logic.BlackKnight import *
from Logic.Director import *

SIZE = 800, 600  # the width and height of our screen
FPS = 20  # Frames per second


class MySprite(pygame.sprite.Sprite):
    def __init__(self, action):
        super(MySprite, self).__init__()
        im = glob.glob(action)
        lenim = len(im[0])
        self.images = [pygame.image.load(img)
                       for img in im if len(img) == lenim]
        self.images2 = [pygame.image.load(img)
                        for img in im if len(img) > lenim]
        self.images.extend(self.images2)
        self.index = 0
        self.rect = pygame.Rect(40, 40, 800, 600)

    def update(self):
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.index += 1


def create_sprites():
    while True:
        director = Director
        opc = int(input(
            "Seleccione el guerrero a su preferencia\n1. para el caballero negro\n2. para el caballero dorado\n"))
        if opc == 1:
            director.setBuilder(director, ConstructorBK())
            iddle = pygame.sprite.Group(director().getknight(0))
            walk = pygame.sprite.Group(director().getknight(1))
            jump = pygame.sprite.Group(director().getknight(2))
            break
        elif opc == 2:
            director.setBuilder(director, ConstructorGK())
            iddle = pygame.sprite.Group(director().getknight(0))
            walk = pygame.sprite.Group(director().getknight(1))
            jump = pygame.sprite.Group(director().getknight(2))
            break
        else:
            print("Por favor ingrese una opción correcta")
    return iddle, walk, jump


def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Patrons")
    iddle, walk, jump = create_sprites()
    my_group = walk
    clock = pygame.time.Clock()
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    my_group = walk
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    my_group = jump
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    my_group = iddle
        my_group.update()
        screen.fill((0, 0, 0))
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
