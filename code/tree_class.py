import matplotlib.pyplot as plt
import matplotlib as mpl

class Node:
    def __init__(self, type_noeud, valeur=None, fils=None):
        '''
        nom: string avec l'étiquette \n
        fils: liste de noeuds fils \n
        parent: noeud parent
        '''
        self.type = type_noeud
        self.valeur = valeur
        self.fils = fils
        self.parent = None

    def add_fils(self, node_f):
        if self.fils is None:
            self.fils = list()

        self.fils.append(node_f)
    
    def add_list_fils(self, list_f):
        self.fils = list_f
    
    def set_parent(self, node_p):
        self.parent = node_p

    def afficher(self):
        if self.valeur :
            return f"{self.type}({self.valeur})"
        return f"{self.valeur}"
        
        

class File(Node):
    def __init__(self, main, classes=None):
        super().__init__("File", fils=classes + [main])

# class Classes(Node):
#     def __init__(self,fils=None, parent=None):
#         super().__init__("Classes", fils, parent)

class Class(Node):
    def __init__(self, ident, extends, decles):
        super().__init__("Class", valeur=ident, fils=decles)
        self.extends = extends

class Class_Main(Node):
    def __init__(self, name, arg, body) :
        super().__init__("MainClass", valeur=name, fils=body)
        self.arg = arg

class Methode(Node) :
    def __init__(self, name, return_type, params, body) :
        super().__init__("Methode", valeur=name, fils=params + body)
        self.return_type = return_type
        self.params = params 
        self.body = body 

class Constructeur(Node) :
    def __init__(self, name, params, body) :
        super().__init__("Constructeur", valeur=name, fils=params + body)
        self.params = params 
        self.body = body

class Champ(Node) : # il s'agit de <decl> => <type> <ident> ;
    def __init__(self, type_name, name) :
        super().__init__("Champ", valeur=name)
        self.type_name = type_name

class Param(Node) :
    def __init__(self, type_name, name) :
        super().__init__("Param", valeur=name)
        self.type_name = type_name



# class Decl(Node):
#     pass

# class Decl_block(Node):
#     def __init__(self):
#         super().__init__("Decl_block", list())

# class Decl_suffix(Node):
#     pass
# class Decl_ident(Node):
#     pass

# class Param_block(Node):
#     def __init__(self):
#         super().__init__("Param_block", list())

# class Param(Node):
#     def __init__(self, ident, type):
#         super().__init__("Param")
#         self.add_list_fils = [Node(type, None, self),Node(ident, None, self)]

# class Params_bis(Node):
#     pass

# class Expr(Node):
#     pass
# class Expr_N1_bis(Node):
#     pass
# class Expr_N2(Node):
#     pass
# class Expr_N2_bis(Node):
#     pass
# class Expr_N3(Node):
#     pass
# class Expr_N3_bis(Node):
#     pass
# class Expr_N4(Node):
#     pass
# class Expr_N4_bis(Node):
#     pass
# class Expr_N5(Node):
#     pass
# class Expr_N5_bis(Node):
#     pass
# class Expr_N6(Node):
#     pass
# class Expr_N6_bis(Node):
#     pass
# class Expr_N7(Node):
#     pass
# class Expr_N7_bis(Node):
#     pass
# class Expr_N8(Node):
#     pass
# class Expr_N9(Node):
#     pass
# class Expr_N9_bis(Node):
#     pass
# class Expr_parenthese(Node):
#     pass
# class Expr_ident(Node):
#     pass
# class Item(Node):
#     pass
# class Expr_bis(Node):
#     pass
# class Lexpr(Node):
#     pass
# class Lexpr_bis(Node):
#     pass
# class Stmt(Node):
#     pass
# class Stmtes(Node):
#     pass
# class Stmt_type(Node):
#     pass
# class Stmt_if(Node):
#     pass

# class Stmt_ident(Node):
#     pass
