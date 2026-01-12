n = 0
from nodes_class import *

class Parseur:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.token = tokens[self.pos]
        self.racine = None

    def lire(self): 
        '''
        avance au token suivant
        '''
        self.pos += 1
        if self.pos < len(self.tokens):
            self.token = self.tokens[self.pos]
        else:
            self.token = ('EOF', 'EOF')

        return self.token

    def reculer(self, n):
        '''
        recule de n tokens
        '''
        if n >= self.pos:
            pass #erreur, on ne peut pas reculer autant
        self.pos -= n
        self.token = self.tokens[self.pos]

        return self.token
    

    def verif_file(self):
        c_l = self.verif_classes()
        ans, n = self.verif_class_main()
        return ans, File(n, c_l)
        

    def verif_classes(self): #boucle while tant qu'on a un class
        var = True
        c_l = []
        while var:
            var, c = self.verif_class()
            if c is not None:
                c_l.append(c)
        return c_l #liste de classes


    def verif_class(self):
        '''
        return noeud class ou None
        '''
        token = self.lire()
        if token[0] == "class":
            token = self.lire()
            if token[1] == "ident":
                if token[0] == "Main":
                    self.reculer(2)
                    return False, None  
                
                else:
                    nom_classe = token[0]
                    token = self.lire()
                    if token[0] == "extends":
                        token = self.lire()
                        if token[1] != "ident":
                            return False, None
                        
                        ext = token[0]
                        token = self.lire()
                    if token[0] == "{":
                        declb = self.verif_decles()
                        token = self.lire()
                        if token[0] == "}":
                            if ext:
                                c = Class(nom_classe, declb, ext)
                            else:
                                c = Class(nom_classe, declb)
                            return True, c
        return("le fichier n'est pas juste", None)

    def verif_decl(self):
        token = self.lire()
        match token[0], token[1]:
            case("void",_):
                token = self.lire()
                if (token[1]=="ident"):
                    token = self.lire()
                    if(token[0]=="("):
                        token = self.lire()
                        if(token[0]!=")"):
                            self.reculer(1)
                            if not self.verif_params():
                                return False, None
                            token = self.lire()
                            if token[0] != ")":
                                return False, None
                        token = self.lire()
                        if(token[0] == "{"):
                            self.verif_stmtes()
                            token = self.lire()
                            if token[0] != "}":
                                return False, None 
            case("boolean",_):
                return(self.verif_ident() and self.verif_decl_suffix())
            case("int",_):
                return(self.verif_ident() and self.verif_decl_suffix())
            case (_,"ident"): 
                return(self.verif_decl_ident())
            case _:
                return False
            
    def verif_decles(self):
        var = True
        l_decl = []
        while var:
            i = n ####################### N EST LA VARIABLE GLOBALE? FAUDRA VERIFIER QUE C'EST BIEN çA BREF
            var, decl = self.verif_decl()
            if decl is not None: 
                l_decl.append(decl)
        n = i
        return DeclBlock(l_decl)
        


    def verif_decl_suffix(self):
        token = self.lire()
        match token[0]:
            case ";":
                return True
            case "(":
                token = self.lire()
                if(token[0]!=")"):
                    self.reculer()
                    if not self.verif_params():
                        return False
                    token = self.lire()
                    if token[0] != ")":
                        return False
                    token = self.lire()
                if token[0] == "{":
                    self.verif_stmtes()
                    token = self.lire()
                    if token[0] == "}":
                        return True
                return False
            case _ :
                return False
            
    #prime devient bis


    def verif_lexpr(self):
        return(self.verif_expr() and self.verif_lexpr_bis())


    ####################################
    def verif_lexpr_bis(self):
        token = self.lire()
        if token[0] == ",":
            return(self.verif_lexpr())
        else:
            self.reculer()
            return True
        
    def verif_stmt(self):
        token = self.lire()
        match token[0], token[1]:
            case ";", _ : 
                return True
            case "if", _:
                token = self.lire()
                if token[0] == "(":
                    if self.verif_expr():
                        token = self.lire()
                        if token[0] == ")":
                            return(self.verif_stmt() and self.verif_stmt_if())
            case "for", _:
                token = self.lire()
                if token[0] == "(":
                    for i in range(2):
                        if(token[0] != ";"):
                            self.reculer()
                            if not self.verif_expr():
                                return False
                        token = self.lire()
                        if token[0] != ";":
                            return False
                        token = self.lire()
                    
                    if not token[0] == ")":
                        self.reculer()
                        if not self.verif_expr():
                            return False
                        token = self.lire()
                    if token[0] == ")":
                        return self.verif_stmt()
            case "{", _:
                if self.verif_stmtes():
                    token = self.lire()
                    return(token[0] == "}")
            case "return", _:
                token = self.lire()
                if token[0] != ";":
                    self.reculer()
                    if not(self.verif_expr()):
                        return False
                    token = self.lire()
                if token[0] == ";":
                    return True
            case "boolean" | "int", _:
                return(self.verif_ident() and self.verif_stmt_type())
            case _,"integer":
                if self.verif_integer():
                    if self.verif_expr_bis():
                        token = self.lire()
                        return(token[0] )== ";"
            case _, "mot":
                if self.verif_string():
                    if self.verif_expr_bis():
                        token = self.lire()
                        return(token[0] )== ";"
            #######################ON POURRAIT LES REGROUPER AVEC UN TRUC EN MODE {token[1]}
            case "true" | "false" | "this " | "new",_:
                if self.verif_expr_bis():
                    token = self.lire()
                    return(token[0] )== ";"
            case "new", _:
                if self.verif_ident():
                    token = self.lire()
                    if token[0] == "(":
                        token = self.lire()
                        if token[0] != ")":
                            self.reculer()
                            if not(self.verif_expr()):
                                return False
                            token = self.lire()
                        if token[0] == ")":
                            if self.verif_expr_bis():
                                token = self.lire()
                                return(token[0] == ";")
            case "!" | "-",_:
                if self.verif_expr():
                    token = self.lire()
                    return(token[0] )== ";"
            case "(", _:
                if(self.verif_expr_parenthese() and self.verif_expr_bis()):
                    token = self.lire()
                    return(token[0] )== ";"
            case _,"ident":
                return(self.verif_stmt_ident())
        return False


    def verif_stmtes(self):
        var = True
        while var:
            i = n ####################### N EST LA VARIABLE GLOBALE? FAUDRA VERIFIER QUE C'EST BIEN çA BREF
            var = self.verif_stmt()
        n = i

    def verif_stmt_type(self):
        token = self.lire()
        match token[0]:
            case ";":
                return True
            case "=":
                if self.verif_expr():
                    token = self.lire()
                    return(token[0] == ";")
        return False


    def verif_if(self):
        token = self.lire()
        if(token[0] == "else"):
            return self.verif_stmt()
        else:
            self.reculer(1)
            return True, None #pas de else stmt
        
    def verif_stmt_ident(self):
        token = self.lire()
        match token[1]:
            case "ident":
                return self.verif_stmt_type()
            case _:
                self.reculer()
                if self.verif_expr_bis():
                    token = self.lire()
                    return(token[0] == ";")