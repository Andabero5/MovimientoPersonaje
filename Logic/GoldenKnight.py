# Concret Builder
from Logic.Knight import *
from Logic.Actions import *


class GoldenKnight(Knight):
    def iddle(self):
        super().iddle()
        i = GKFactory()
        return i.createIddleAction()

    def walk(self):
        super().walk()
        w = GKFactory()
        return w.createWalkAction()

    def jump(self):
        super().jump()
        j = GKFactory()
        return j.createJumpAction()

    def set_sprites(self, images):
        return super().set_sprites(images)
