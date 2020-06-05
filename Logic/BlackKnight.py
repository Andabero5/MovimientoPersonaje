# Concret Builder
from Logic.Knight import *
from Logic.Actions import *


class BlackKnight(Knight):
    '''
    Concrete Factory Black Knight
    '''

    def iddle(self):
        super().iddle()
        i = BKFactory()
        return i.createIddleAction()

    def walk(self):
        super().walk()
        w = BKFactory()
        return w.createWalkAction()

    def jump(self):
        super().jump()
        j = BKFactory()
        return j.createJumpAction()
