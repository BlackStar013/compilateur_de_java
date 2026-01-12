class Node:
    def __init__(self, name, fils=None):
        '''
        valeur: string avec l'étiquette \n
        fils: liste de noeuds fils \n
        '''
        self.name = name
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

    # def afficher(self):
    #     if self.valeur :
    #         return f"{self.type}({self.valeur})"
    #     return f"{self.valeur}"
        

# Structures <file>, <class>, <decl>

class File(Node):
    def __init__(self, main, classes=None):
        super().__init__("File", fils = [classes, main])

# class Classes(Node):
#     def __init__(self,fils=None, parent=None):
#         super().__init__("Classes", fils, parent)

class Class(Node):
    def __init__(self, ident, decles, extends=None): # Revenir sur decles
        fils = [Node(ident)]
        if extends :
            n_extends = Node(f"extends {extends}")
            fils.append(n_extends)
        fils.append(decles)
        
        super().__init__("Class", fils=fils)

class Class_Main(Node):
    def __init__(self, ident, StmtBlock) :
        fils = [Node(ident), StmtBlock]
        super().__init__("MainClass", fils=fils)

class Methode(Node) :
    def __init__(self, ident, return_type, StmtBlock, params=None) :
        fils = [Node(return_type), Node(ident)]
        if params :
            fils.append(params)
        fils.append(StmtBlock)
        super().__init__("Methode", fils=fils)

class Constructeur(Node) :
    def __init__(self, ident, StmtBlock, params=None) :
        fils = [Node(ident)]
        if params :
            fils.append(params)
        fils.append(StmtBlock)
        super().__init__("Constructeur", fils=fils)

class Champ(Node) : # il s'agit de <decl> => <type> <ident> ;
    def __init__(self, type_ident, ident) :
        fils = [Node(type_ident), Node(ident)]
        super().__init__("Champ", fils=fils)

class ParamBlock(Node) :
    def __init__(self, params) :
        '''
        params: liste de noeuds param ??? \n
        '''
        super().__init__("ParamBlock", fils=params)

class Param(Node) :
    def __init__(self, type_ident, ident) :
        fils = [Node(type_ident), Node(ident)]
        super().__init__("Param", fils=fils)


# Stmt

class StmtBlock(Node) : 
    def __init__(self, stmts) :
        '''
        stmts: liste de noeuds \n
        '''
        super().__init__("StmtBlock", fils=stmts)

class If(Node) : # if (<expr>) <stmt> (else <stmt>)?
    def __init__(self, cond, then_stmt, else_stmt=None) :
        fils = [cond, then_stmt]
        if else_stmt :
            fils.append(else_stmt)
        super().__init__("If", fils=fils)

class For(Node) : # for (<expr>?; <expr>?; <expr>?) <stmt>
    def __init__(self, init, cond, maj, StmtBlock) : # peut être mettre init cond et maj par défaut à None
        fils = [init, cond, maj, StmtBlock]
        super().__init__("For", fils=fils)

class Return(Node) : # return <expr>? ;
    def __init__(self, expr=None) :
        fils = None
        if expr :
            fils = [expr]
        super().__init__("Return", fils=fils)

class ExprVar(Node) : #<stmt> -> <type> <ident> (= <expr>)? ;
    def __init__(self, type_ident, ident, expr=None) :
        fils = [Node(type_ident), Node(ident)] 
        if expr :
            fils.append(expr)
        super().__init__("ExprVar", fils=fils)

class ExprStmt(Node) : # <expr> ;
    def __init__(self, expr) :
        super().__init__("Expr", fils=[expr])

class EmptyStmt(Node) : # ;
    def __init__(self) :
        super().__init__("Empty")


# Expression

class Attribution(Node) : # <expr_N1'>
    def __init__(self, left_expr, right_expr) :
        fils = [left_expr, right_expr]
        super().__init__("Attribution", fils=fils)

class Binop(Node) : # 2 à 7
    def __init__(self, op, left_exp, right_exp) :
        fils = [left_exp, right_exp]
        super().__init__(op, fils=fils)

class Unop(Node) : # -, !
    def __init__(self, op, expr) :
        super().__init__(op, fils=[expr])

class Instanceof(Node) : # instanceof <type> <expr_N5'> , mouette
    def __init__(self, type, expr) :
        fils = [expr, Node(type)]
        super().__init__("Instanceof", fils=fils)

class Cast(Node): # pas sûr
    def __init__(self, target_type, expr):
        # target_type : le nom du type vers lequel on convertit (ex: "int", "String")
        # expr : le noeud AST de l'expression à convertir
        super().__init__("Cast", valeur=target_type, fils=[expr])

class New(Node) : # <item> => new <ident>(...)
    def __init__(self, name, args) :
        super().__init__("New", valeur=name, fils=args)

class AppelMethode(Node) : # pas sûr

    def __init__(self, obj, name, args) :
        # obj : Le noeud de l'objet sur lequel on appelle la méthode.
        # Si l'appel est "maMethode()", obj sera souvent un noeud "Literal:this" ou None.
        # method_name : Le nom de la fonction (string)
        # args : Liste des noeuds AST des arguments
        fils = []
        if obj :
            fils = [obj]
        fils = fils + args 
        super().__init__("AppelMethode", valeur=name, fils=fils)

class AccesChamp(Node) : # pas sûr
    def __init__(self, obj, name) :
        # obj : Le noeud de l'expression avant le point
        # field_name : Le nom de l'attribut accédé (string)
        super().__init__("AccesChamp", valeur=name, fils=[obj])

class Element(Node) : # <item> => <integer> | <string> | true | false | this | null
    def __init__(self, type_lit, val) :
        super().__init__("Element", valeur=f"{type_lit}:{val}")

class Ident(Node) : # <item> => <ident>
    def __init__(self, name) :
        super().__init__("Ident", valeur=name) 

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
