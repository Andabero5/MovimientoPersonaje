import pygame


class Derecha():
    def get_sprites(self):
        pass


class DerechaZombi(Derecha):
    def get_sprites(self):
        return [pygame.image.load('Personaje_master\Img\spritesZ\ZCD1.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCD2.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCD3.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCD4.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCD5.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCD6.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCD7.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCD8.png')]


class Izquierda():
    def get_sprites(self):
        pass


class IzquierdaZombi(Izquierda):
    def get_sprites(self):
        return [pygame.image.load('Personaje_master\Img\spritesZ\ZCI1.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCI2.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCI3.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCI4.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCI5.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCI6.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCI7.png'),
                pygame.image.load('Personaje_master\Img\spritesZ\ZCI8.png')]
