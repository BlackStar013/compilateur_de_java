class Node:
    def __init__(self,position):
        '''
        position: ligne
        '''
        self.position = position

class File:
    '''
    root de tous les fichier
    '''
    def __init__(self,classes, main_class, position=None):
        super().__init__(position)
        self.classes = classes #liste de classes dans le fichier
        self.main_class = main_class #noeud Main_class

class Class: pass

class Main_class:
    def __init__(self,arg, stmts, position=None):
        super.__init__(position)
        self.arg = arg
        self.stmts = stmts #liste de noeuds stmt ou noeud stmts qui à son tour à des fils stmt

