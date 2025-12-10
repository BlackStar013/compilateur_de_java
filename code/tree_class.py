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
        

# Structures <file>, <class>, <decl>

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


# Stmt

class Stmtes(Node) : 
    def __init__(self, stmts) :
        super.__init__("Stmtes", fils=stmts)

class If(Node) : # if (<expr>) <stmt> (else <stmt>)?
    def __init__(self, cond, then_stmt, else_stmt=None) :
        fils = [cond, then_stmt]
        if else_stmt :
            fils.append(else_stmt)
        super().__init__("If", fils=fils)

class For(Node) : # for (<expr>?; <expr>?; <expr>?) <stmt>
    def __init__(self, init, cond, maj, body) : # peut être mettre init cond et maj par défaut à None
        fils = [init, cond, maj, body]
        super().__init__("For", fils=fils)

class Return(Node) : # return <expr>?
    def __init__(self, expr=None) :
        fils = None
        if expr :
            fils = [expr]
        super().__init__("Return", fils=fils)

class ExprVar(Node) : # <type> <ident> (= <expr>)? ;
    def __init__(self, type_name, name, expr=None) :
        fils = None 
        if expr :
            fils = [expr]
        super().__init__("ExprVar", valeur=name, fils=fils)
        self.type_name = type_name

class ExprStmt(Node) : # <expr> ;
    def __init__(self, expr) :
        super().__init__("Expr", fils = [expr])

class EmptyStmt(Node) : # ;
    def __init__(self) :
        super().__init__("Empty")


# Expression

class Binop(Node) : # 2 à 7
    def __init__(self, op, left, right) :
        super().__init__("Binop", valeur=op, fils=[left, right])

class Unop(Node) : # -, !
    def __init__(self, op, expr) :
        super().__init__("Unop", valeur=op, fils=[expr])

class Instanceof(Node) : # instanceof <type> <expr_N5'> , mouette
    def __init__(self, type_name, expr) :
        super().__init__("Instanceof", valeur=type_name, fils=[expr])

# class Parenthese(Node) : 
#     def __init__(self,)

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
# class Stmt_type(Node):
#     pass
# class Stmt_if(Node):
#     pass

# class Stmt_ident(Node):
#     pass
