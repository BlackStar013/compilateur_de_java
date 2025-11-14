class Node:
    def __init__(self,nom,fils):
        '''
        
        '''
        self.nom = nom #le type
        self.fils = fils #liste des fils

class File:
    '''
    root de tous les fichier
    '''
    def __init__(self,classes, main_class, fils=None):
        super().__init__("fichier", fils)
        self.classes = classes #liste de classes dans le fichier
        self.main_class = main_class #noeud Main_class

class Class: pass

class Main_class:
    def __init__(self,arg, stmts, position=None):
        super.__init__(position)
        self.arg = arg
        self.stmts = stmts #liste de noeuds stmt ou noeud stmts qui à son tour à des fils stmt

