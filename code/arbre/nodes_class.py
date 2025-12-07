import matplotlib.pyplot as plt
import matplotlib as mpl

class Node:
    def __init__(self,nom, parent=None, fils=None):
        '''
        nom: string avec l'étiquette \n
        fils: liste de noeuds fils \n
        parent: noeud parent
        '''
        self.nom = nom 
        self.parent = parent
        self.fils = fils

    def add_fils(self, node_f):
        if self.fils is None:
            self.fils = list()

        self.fils.append(node_f)
    
    def add_list_fils(self, list_f):
        self.fils = list_f
    
    def set_parent(self, node_p):
        self.parent = node_p

    def afficher(self):
        print(self.nom)
        
        

class File(Node):
    def __init__(self, main, classes=None):
        super().__init__("File", None, list((classes, main)))

class Classes(Node):
    def __init__(self):
        super().__init__("Classes", None, list())

class Class(Node):
    def __init__(self, ident):
        super().__init__("Class", None, [Node(ident,self)])

class Decl(Node):
    pass

class Decl_block(Node):
    def __init__(self):
        super().__init__("Decl_block", None, list())

class Decl_suffix(Node):
    pass
class Decl_ident(Node):
    pass

class Param_block(Node):
    def __init__(self):
        super().__init__("Param_block", None, list())

class Param(Node):
    def __init__(self, ident, type):
        super().__init__("Param",None,[Node(type, self),Node(ident,self)])

class Params_bis(Node):
    pass

class Class_Main(Node):
    pass

class Expr(Node):
    pass
class Expr_N1_bis(Node):
    pass
class Expr_N2(Node):
    pass
class Expr_N2_bis(Node):
    pass
class Expr_N3(Node):
    pass
class Expr_N3_bis(Node):
    pass
class Expr_N4(Node):
    pass
class Expr_N4_bis(Node):
    pass
class Expr_N5(Node):
    pass
class Expr_N5_bis(Node):
    pass
class Expr_N6(Node):
    pass
class Expr_N6_bis(Node):
    pass
class Expr_N7(Node):
    pass
class Expr_N7_bis(Node):
    pass
class Expr_N8(Node):
    pass
class Expr_N9(Node):
    pass
class Expr_N9_bis(Node):
    pass
class Expr_parenthese(Node):
    pass
class Expr_ident(Node):
    pass
class Item(Node):
    pass
class Expr_bis(Node):
    pass
class Lexpr(Node):
    pass
class Lexpr_bis(Node):
    pass
class Stmt(Node):
    pass
class Stmtes(Node):
    pass
class Stmt_type(Node):
    pass
class Stmt_if(Node):
    pass

class Stmt_ident(Node):
    pass