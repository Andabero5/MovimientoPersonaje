# Class Director implementa la clase abstracta
from Logic.Knight import *
from Game import *


class Director:

    '''
    Implementa el constructor y retorna el producto
    '''
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getknight(self, num):
        sprite = self.__builder.get_sprites()
        knight = MySprite(sprite[num])
        return knight


class Constructor():
    def get_sprites(self): pass


class ConstructorBK():
    '''
    Construir los personajes a partir de las fabrica BK
    '''

    def __init__(self):
        self.factory = BKFactory()

    def get_sprites(self):
        return[self.factory.createIddleAction(),
               self.factory.createWalkAction(),
               self.factory.createJumpAction()
               ]


class ConstructorGK():
    '''
    Construir los personajes a partir de las fabrica BK
    '''

    def __init__(self):
        self.factory = GKFactory()

    def get_sprites(self):
        return[self.factory.createIddleAction(),
               self.factory.createWalkAction(),
               self.factory.createJumpAction()]
