n = 0

class Parseur:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = -1
        self.token = tokens[self.pos]

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

    #################################

    def verif_file(self):
        print("passage verif_file")
        # print(self.token)
        return(self.verif_classes() and self.verif_class_Main()) #il y a plusieurs class


    def verif_classes(self): #boucle while tant qu'on a un class
        print("passage verif_classes")
        var = True
        while var:
            i = self.pos
            var = self.verif_class()
        self.pos = i
        return True


    def verif_class(self):
        print("passage verif_class")
        token = self.lire()
        if token[0] == "class":
            token = self.lire()
            if token[1] == "ident":
                if token[0] == "Main":
                    token = self.reculer(2)
                    return False
                else:
                    token = self.lire()
                    if token[0] == "extends":
                        token = self.lire()
                        if token[1] != "ident":
                            return False
                        token = self.lire()
                    if token[0] == "{":
                        if self.verif_decles():
                            token = self.lire()
                            if token[0] == "}":
                                return True
        return False
        # return("le fichier n'est pas juste")

    def verif_decl(self):
        print("passage verif_decl")
        token = self.lire()
        match token[0], token[1]:
            case("void",_):
                token = self.lire()
                if (token[1]=="ident"):
                    token = self.lire()
                    if(token[0]=="("):
                        token = self.lire()
                        print(token)
                        if(token[0]!=")"):
                            token = self.reculer(1)
                            if(not self.verif_params()):
                                return False
                            token = self.lire()
                            if(token[0] != ")"):
                                return False
                        token = self.lire()
                        print(token)
                        if(token[0] == "{"):
                            token = self.lire()
                            print(token)
                            if(token[0]!="}"):
                                token = self.reculer(1)
                                if not self.verif_stmtes():
                                    return False
                                token = self.lire()
                                if token[0] != "}":
                                    return False
                            return True
            case("boolean",_):
                token = self.lire()
                if(token[1] == "ident"):
                    return self.verif_decl_suffix()
                return False
            case("int",_):
                token = self.lire()
                if(token[1] == "ident"):
                    return self.verif_decl_suffix()
            case (_,"ident"): 
                return(self.verif_decl_ident())
            case _:
                return False

    def verif_decles(self):
        print("passage verif_decles")
        var = True
        while var:
            i = self.pos 
            var = self.verif_decl()
        self.pos = i
        return True


    def verif_decl_suffix(self):
        print("passage verif_decl_suffix")
        token = self.lire()
        match token[0]:
            case ";":
                return True
            case "(":
                token = self.lire()
                if(token[0]!=")"):
                    token = self.reculer(1)
                    if not self.verif_params():
                        return False
                    token = self.lire()
                    if token[0] != ")":
                        return False
                    token = self.lire()
                if token == "{":
                    self.verif_stmtes()
                    token = self.lire()
                    if token[0] == "}":
                        return True
                return False
            case _ :
                return False

    #prime devient bis

    def verif_decl_ident(self):
        print("passage verif_decl_ident")
        token = self.lire()
        if(token[1] == "ident"):
            return self.verif_decl_suffix()
        elif(token[0] == "("):
            token = self.lire()
            if(token[0] != ")"):
                token = self.reculer(1)
                if(not self.verif_params()):
                    return False
                token = self.lire()
                if(token[0] != ")"):
                    return False
                token = self.lire()
                if(token[0] == "{"):
                    token = self.lire()
                    if(token[0]!="}"):
                        token = self.reculer(1)
                        if not self.verif_stmtes():
                            return False
                        token = self.lire()
                        if token[0] != "}":
                            return False

    def verif_params(self):
        print("passage verif_params")
        if(self.verif_type()):
            token = self.lire()
            if(token[1] == "ident"):
                return self.verif_params_bis()

    def verif_params_bis(self):
        print("passage verif_params_bis")
        token = self.lire()
        if(token[0] == ","):
            return self.verif_params()
        return True

    def verif_type(self):
        print("passage verif_type")
        token = self.lire()
        if(token[1] == "boolean" or token[1] == "int" or token[1] == "ident"):
            return True
        return False

    def verif_class_Main(self):
        print("passage verif_class_Main")
        token = self.lire()
        if(token[0] == "class"):
            token = self.lire()
            if(token[0] == "Main"):
                token = self.lire()
                if(token[0] == "{"):
                    token = self.lire()
                    if(token[0] == "public"):
                        token = self.lire()
                        if(token[0] == "static"):
                            token = self.lire()
                            if(token[0] == "void"):
                                token = self.lire()
                                if(token[0] == "main"):
                                    token = self.lire()
                                    if(token[0] == "("):
                                        token = self.lire()
                                        if(token[0] == "String"):
                                            token = self.lire()
                                            if(token[1] == "ident"):
                                                token = self.lire()
                                                if(token[0] == "["):
                                                    token = self.lire()
                                                    if(token[0] == "]"):
                                                        token = self.lire()
                                                        if(token[0] == ")"):
                                                            token = self.lire()
                                                            if(token[0] == "{"):
                                                                token = self.lire()
                                                                if(token[0]!="}"):
                                                                    token = self.reculer(1)
                                                                    if not self.verif_stmtes():
                                                                        return False
                                                                    token = self.lire()
                                                                    if token[0] != "}":
                                                                        return False
                                                                    token = self.lire()
                                                                    if(token[0] == "}"):
                                                                        return True
                                                                elif(token[0] == "}"):
                                                                    return True
        return False

    def verif_expr(self) :
        print("passage verif_expr")
        return (self.verif_expr_N2() and self.verif_expr_N1_bis())
    
    def verif_expr_N1_bis(self) :
        print("passage verif_expr_N1_bis")
        token = self.lire()
        if token[0] == '=' :
            return(self.verif_expr())
        else :
            token = self.reculer(1)
            return True 
        
    def verif_expr_N2(self) :
        print("passage verif_expr_N2")
        return (self.verif_expr_N3() and self.verif_expr_N2_bis())
    
    def verif_expr_N2_bis(self) :
        print("passage verif_expr_N2_bis")
        token = self.lire()
        if token[0] == '||' :
            return(self.verif_expr_N3() and self.verif_expr_N2_bis())
        else :
            token = self.reculer(1)
            return True 
        
    def verif_expr_N3(self) :
        print("passage verif_expr_N3")
        return (self.verif_expr_N4() and self.verif_expr_N3_bis())
    
    def verif_expr_N3_bis(self) :
        print("passage verif_expr_N3_bis")
        token = self.lire()
        if token[0] == '&&' :
            return (self.verif_expr_N4() and self.verif_expr_N3_bis())
        else :
            token = self.reculer(1)
            return True
        
    def verif_expr_N4(self) :
        print("passage verif_expr_N4")
        return (self.verif_expr_N5() and self.verif_expr_N4_bis())
    
    def verif_expr_N4_bis(self) :
        print("passage verif_expr_N4_bis")
        token = self.lire()
        match token[0] :
            case "==" :
                return (self.verif_expr_N5() and self.verif_expr_N4_bis())
            case "!=" :
                return (self.verif_expr_N5() and self.verif_expr_N4_bis())
            case _ :
                token = self.reculer(1)
                return True 
            
    def verif_expr_N5(self) :
        print("passage verif_expr_N5")
        return (self.verif_expr_N6() and self.verif_expr_N5_bis())
    
    def verif_expr_N5_bis(self) :
        print("passage verif_expr_N5_bis")
        token = self.lire()
        match token[0] :
            case "<" :
                return (self.verif_expr_N6() and self.verif_expr_N5_bis())
            case "<=" :
                return (self.verif_expr_N6() and self.verif_expr_N5_bis())
            case ">" :
                return (self.verif_expr_N6() and self.verif_expr_N5_bis())
            case ">=" :
                return (self.verif_expr_N6() and self.verif_expr_N5_bis())
            case "instanceof" :
                return (self.verif_type() and self.verif_expr_N5_bis())
            case _ :
                token = self.reculer(1)
                return True 
            
    def verif_expr_N6(self) :
        print("passage verif_expr_N6")
        return (self.verif_expr_N7() and self.verif_expr_N6_bis())
    
    def verif_expr_N6_bis(self) :
        print("passage verif_expr_N6_bis")
        token = self.lire()
        match token[0] :
            case "+" :
                return (self.verif_expr_N7() and self.verif_expr_N6_bis())
            case "-" :
                return (self.verif_expr_N7() and self.verif_expr_N6_bis())
            case _ :
                token = self.reculer(1)
                return True 
    
    def verif_expr_N7(self) :
        print("passage verif_expr_N7")
        return (self.verif_expr_N8() and self.verif_expr_N7_bis())
    
    def verif_expr_N7_bis(self) :
        print("passage verif_expr_N7_bis")
        token = self.lire()
        match token[0] :
            case "*" :
                return (self.verif_expr_N8() and self.verif_expr_N7_bis())
            case "//" :
                return (self.verif_expr_N8() and self.verif_expr_N7_bis())
            case "%" :
                return (self.verif_expr_N8() and self.verif_expr_N7_bis())
            case _ :
                token = self.reculer(1)
                return True 
            
    def verif_expr_N8(self) :
        print("passage verif_expr_N8")
        token = self.lire()
        match token[0] :
            case "!" :
                return (self.verif_expr_N8())
            case "-" :
                return (self.verif_expr_N8())
            case "(" :
                return (self.verif_expr_parenthese())
            case _ :
                token = self.reculer(1)
                return (self.verif_expr_N9())

    def verif_expr_N9(self) :
        print("passage verif_expr_N9")
        return (self.verif_item() and self.verif_expr_N9_bis())
    
    def verif_expr_N9_bis(self) :
        print("passage verif_expr_N9_bis")
        token = self.lire()
        match token[0] :
            case "." :
                token = self.lire()
                if token[1] == "ident" :
                    return self.verif_expr_ident()
                return False
            case "(" :
                token = self.lire()
                if token[0] != ")" :
                    token = self.reculer(1)
                    if not self.verif_lexpr() :
                        return False
                    token = self.lire()
                if token[0] == ")" :
                    return self.verif_expr_N9_bis()
                return False 
            case _ :
                token = self.reculer(1)
                return True
            
    def verif_expr_ident(self) :
        print("passage verif_expr_ident")
        token = self.lire()
        if token[0] == '=' :
            return self.verif_expr()
        else :
            token = self.reculer(1)
            return self.verif_expr_N9_bis()
        
    def verif_item(self) :
        print("passage verif_item")
        token = self.lire()
        match token[0], token[1] :
            case _, "integer" :
                return True 
            case _, "string" :
                return True 
            case "true", _ :
                return True
            case "false", _ :
                return True 
            case "this", _ :
                return True
            case "null", _ :
                return True 
            case "new", _ :
                token = self.lire()
                if token[1] == "ident" :
                    token = self.lire()
                    if token[0] == "(" :   
                        token = self.lire()
                        if token[0] != ")" :
                            token = self.reculer(1)
                            if not self.verif_lexpr() :
                                return False
                            token = self.lire()
                        if token[0] == ")" :
                            return True 
            case _, "ident" :
                return True 
    
    
   # def verif_expr_parenthese(self) :  cas à compléter 2
        
    def verif_expr_bis(self) :
        print("passage verif_expr_bis")
        return (self.verif_expr_N9_bis() and self.verif_expr_N7_bis() and self.verif_expr_N6_bis() and self.verif_expr_N5_bis() and self.verif_expr_N4_bis() and self.verif_expr_N3_bis() and self.verif_expr_N2_bis() and self.verif_expr_N1_bis())


    def verif_lexpr(self):
        print("passage verif_lexpr")
        return(self.verif_expr() and self.verif_lexpr_bis())

    def verif_lexpr_bis(self):
        print("passage verif_lexpr_bis")
        token = self.lire()
        if token[0] == ",":
            return(self.verif_lexpr())
        else:
            token = self.reculer(1)
            return True
        
    def verif_stmt(self):
        print("passage verif_stmt")
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
                            token = self.reculer(1)
                            if not self.verif_expr():
                                return False
                        token = self.lire()
                        if token[0] != ";":
                            return False
                        token = self.lire()
                    
                    if not token[0] == ")":
                        token = self.reculer(1)
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
                    token = self.reculer(1)
                    if not(self.verif_expr()):
                        return False
                    token = self.lire()
                if token[0] == ";":
                    return True
            case "boolean" | "int", _:
                token = self.lire()
                if(token[1] == "ident"):
                    return(self.verif_stmt_type())
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
                token = self.lire()
                if(token[0] == "ident"):
                    token = self.lire()
                    if token[0] == "(":
                        token = self.lire()
                        if token[0] != ")":
                            token = self.reculer(1)
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
        print("passage verif_stmtes")
        var = True
        while var:
            i = self.pos ####################### N EST LA VARIABLE GLOBALE? FAUDRA VERIFIER QUE C'EST BIEN çA BREF
            var = self.verif_stmt()
        self.pos = i
        return True

    def verif_stmt_type(self):
        print("passage verif_stmt_type")
        token = self.lire()
        match token[0]:
            case ";":
                return True
            case "=":
                if self.verif_expr():
                    token = self.lire()
                    return(token[0] == ";")
        return False



    def verif_stmt_if(self):
        print("passage verif_if")
        token = self.lire()
        if(token[0] == "else"):
            return self.verif_stmt()
        else:
            token = self.reculer(1)
            return True
        
    def verif_stmt_ident(self):
        print("passage verif_stmt_ident")
        token = self.lire()
        match token[1]:
            case "ident":
                return self.verif_stmt_type()
            case _:
                token = self.reculer(1)
                if self.verif_expr_bis():
                    token = self.lire()
                    return(token[0] == ";")
