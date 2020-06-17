# Class Director implementa la clase abstracta
from Logic.Knight import *
from Game import *
from Logic.Adapter import *
from Personaje_master.constuctores import *


class Director():

    '''
    Implementa el constructor y retorna el producto
    '''

    def setBuilder(self, builder):
        self.__builder = builder

    def getknight(self, num):
        sprite = self.__builder.get_sprites()
        if type(self.__builder) != ConstructorZM:
            knight = MySprite(sprite[num])
        else:
            knight = MySpriteAdapter(sprite[num])
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


class ConstructorZM():
    def __init__(self):
        self.factory = ConstructorZombis()

    def get_sprites(self):
        return self.factory.get_sprites()
