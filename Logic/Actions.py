# ABSTRACT FACTORY
class Actions():
    '''
    clase abstracta que crea las acciones 
    '''

    def createJumpAction(self): pass

    def createWalkAction(self): pass

    def createIddleAction(self): pass

# GOLDEN KNIGHT FACTORY


class GKFactory(Actions):
    '''
    Concrete factory de golden knight donde se setean las acciones
    '''

    def createIddleAction(self):
        super().createIddleAction()
        return "GKImages/iddle*.png"

    def createWalkAction(self):
        super().createWalkAction()
        return "GKImages/walk*.png"

    def createJumpAction(self):
        super().createJumpAction()
        return "GKImages/jump*.png"


# BLACK KNIGHT FACTORY
class BKFactory(Actions):
    '''
    Concrete factory de black knight donde se setean las acciones
    '''

    def createIddleAction(self):
        super().createIddleAction()
        return "BKImages/iddle*.png"

    def createWalkAction(self):
        super().createWalkAction()
        return "BKImages/walk*.png"

    def createJumpAction(self):
        super().createJumpAction()
        return "BKImages/jump*.png"
