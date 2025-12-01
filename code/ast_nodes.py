class Node:
    def __init__(self,nom, parent=None, fils=None):
        '''
        nom: string avec l'étiquette
        fils: liste de noeuds fils
        parent: noeud parent
        '''
        self.nom = nom 
        self.parent = parent
        self.fils = fils

    def add_fils(self, node_f):
        self.fils.append(node_f)
    
    def set_parent(self, node_p):
        self.parent = node_p

    def afficher(self):
        print(self.nom)

class File(Node):
    def __init__(self, main, classes=None):
        super().__init__("File", None, list(main, classes))
        self.main = main
        self.classes = classes

class Classes(Node):
    def __init__(self):
        super().__init__("Classes", None, list())

class Class(Node):
    def __init__(self):
        super().__init__("Class", None, list())