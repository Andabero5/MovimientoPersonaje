#ABSTRACT FACTORY
class Actions():
    def createJumpAction(self): pass

    def createWalkAction(self): pass

    def createIddleAction(self): pass
    
#GOLDEN KNIGHT FACTORY
class GKFactory(Actions):
    def createIddleAction(self):
        super().createIddleAction()
        return "GKImages/iddle*.png"

    def createWalkAction(self):
        super().createWalkAction()
        return "GKImages/walk*.png"

    def createJumpAction(self):
        super().createJumpAction()
        return "GKImages/jump*.png"


#BLACK KNIGHT FACTORY
class BKFactory(Actions):
    def createIddleAction(self):
        super().createIddleAction()
        return "BKImages/iddle*.png"

    def createWalkAction(self):
        super().createWalkAction()
        return "BKImages/walk*.png"

    def createJumpAction(self):
        super().createJumpAction()
        return "BKImages/jump*.png"

        