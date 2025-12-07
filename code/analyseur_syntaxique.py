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
        self.verif_classes()
        return(self.verif_class_main())
        

    def verif_classes(self): #boucle while tant qu'on a un class
        var = True
        while var:
            var = self.verif_class()
        return


    def verif_class(self):
        token = self.lire()
        if token[0] == "class":
            token = self.lire()
            if token[1] == "ident":
                if token[0] == "Main":
                    self.reculer(2)
                    return False
                else:
                    token = self.lire()
                    if token[0] == "extends":
                        token = self.lire()
                        if token[1] != "ident":
                            return False
                        token = self.lire()
                    if token[0] == "{":
                        self.verif_decles()
                        token = self.lire()
                        if token[0] == "}":
                            return True
        return("le fichier n'est pas juste")

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
                                return False
                            token = self.lire()
                            if token[0] != ")":
                                return False
                        token = self.lire()
                        if(token[0] == "{"):
                            self.verif_stmtes()
                            token = self.lire()
                            if token[0] != "}":
                                return False 
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
        while var:
            i = n ####################### N EST LA VARIABLE GLOBALE? FAUDRA VERIFIER QUE C'EST BIEN çA BREF
            var = self.verif_decl()
        n = i
        


    def verif_decl_suffix(self):
        token = self.lire()
        match token[0]:
            case ";":
                return True
            case "(":
                token = self.lire()
                if(token[0]!=")"):
                    self.reculer(1)
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

    def verif_expr(self) :
        return (self.verif_expr_N2() and self.verif_expr_N1_bis())
    
    def verif_expr_N1_bis(self) :
        token = self.lire()
        if token[0] == '=' :
            return(self.verif_expr())
        else :
            self.reculer(1)
            return True 
        
    def verif_expr_N2(self) :
        return (self.verif_expr_N3() and self.verif_expr_N2_bis())
    
    def verif_expr_N2_bis(self) :
        token = self.lire()
        if token[0] == '||' :
            return(self.verif_expr_N3() and self.verif_expr_N2_bis())
        else :
            self.reculer(1)
            return True 
        
    def verif_expr_N3(self) :
        return (self.verif_expr_N4() and self.verif_expr_N3_bis())
    
    def verif_expr_N3_bis(self) :
        token = self.lire()
        if token[0] == '&&' :
            return (self.verif_expr_N4() and self.verif_expr_N3_bis())
        else :
            self.reculer(1)
            return True
        
    def verif_expr_N4(self) :
        return (self.verif_expr_N5() and self.verif_expr_N4_bis())
    
    def verif_expr_N4_bis(self) :
        token = self.lire()
        match token[0] :
            case "==" :
                return (self.verif_expr_N5() and self.verif_expr_N4_bis())
            case "!=" :
                return (self.verif_expr_N5() and self.verif_expr_N4_bis())
            case _ :
                self.reculer(1)
                return True 
            
    def verif_expr_N5(self) :
        return (self.verif_expr_N6() and self.verif_expr_N5_bis())
    
    def verif_expr_N5_bis(self) :
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
                self.reculer(1)
                return True 
            
    def verif_expr_N6(self) :
        return (self.verif_expr_N7() and self.verif_expr_N6_bis())
    
    def verif_expr_N6_bis(self) :
        token = self.lire()
        match token[0] :
            case "+" :
                return (self.verif_expr_N7() and self.verif_expr_N6_bis())
            case "-" :
                return (self.verif_expr_N7() and self.verif_expr_N6_bis())
            case _ :
                self.reculer(1)
                return True 
    
    def verif_expr_N7(self) :
        return (self.verif_expr_N8() and self.verif_expr_N7_bis())
    
    def verif_expr_N7_bis(self) :
        token = self.lire()
        match token[0] :
            case "*" :
                return (self.verif_expr_N8() and self.verif_expr_N7_bis())
            case "//" :
                return (self.verif_expr_N8() and self.verif_expr_N7_bis())
            case "%" :
                return (self.verif_expr_N8() and self.verif_expr_N7_bis())
            case _ :
                self.reculer(1)
                return True 
            
    def verif_expr_N8(self) :
        token = self.lire()
        match token[0] :
            case "!" :
                return (self.verif_expr_N8())
            case "-" :
                return (self.verif_expr_N8())
            case "(" :
                return (self.verif_expr_parenthese())
            case _ :
                self.reculer(1)
                return (self.verif_expr_N9())

    def verif_expr_N9(self) :
        return (self.verif_item() and self.verif_expr_N9_bis())
    
    def verif_expr_N9_bis(self) :
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
                    self.reculer(1)
                    if not self.verif_lexpr() :
                        return False
                    token = self.lire()
                if token[0] == ")" :
                    return self.verif_expr_N9_bis()
                return False 
            case _ :
                self.reculer(1)
                return True
            
    def verif_expr_ident(self) :
        token = self.lire()
        if token[0] == '=' :
            return self.verif_expr()
        else :
            self.reculer(1)
            return self.verif_expr_N9_bis()
        
    def verif_item(self) :
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
                            self.reculer(1)
                            if not self.verif_lexpr() :
                                return False
                            token = self.lire()
                        if token[0] == ")" :
                            return True 
            case _, "ident" :
                return True 
    
    def verif_expr_parenthese(self) : 
        save_pos = self.pos
        token = self.lire()
        maybe_type = False
        if (token[0] in ["boolean", "int"] or token[1] == "ident") :
            maybe_type = True 
        if maybe_type :
            next_token = self.lire() 
            if next_token[0] == ")" :
                if self.verif_expr_N8() :
                    return True 
                else :  # Il faut reculer de l'ensemble des éléments testés dans self.verif_expr_N8
                    new_pos = self.pos
                    self.reculer(new_pos - save_pos - 1)
            else : 
                self.reculer(1)
        self.reculer(1)
        if self.verif_expr() :
            token = self.lire()
            if token[0] == ")" :
                return True 
            else :
                return False 
        else :
            return False
        
    def verif_expr_bis(self) :
        return (self.verif_expr_N9_bis() and self.verif_expr_N7_bis() and self.verif_expr_N6_bis() and self.verif_expr_N5_bis() and self.verif_expr_N4_bis() and self.verif_expr_N3_bis() and self.verif_expr_N2_bis() and self.verif_expr_N1_bis())

    def verif_lexpr(self):
        return(self.verif_expr() and self.verif_lexpr_bis())


    ####################################
    def verif_lexpr_bis(self):
        token = self.lire()
        if token[0] == ",":
            return(self.verif_lexpr())
        else:
            self.reculer(1)
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
                            self.reculer(1)
                            if not self.verif_expr():
                                return False
                        token = self.lire()
                        if token[0] != ";":
                            return False
                        token = self.lire()
                    
                    if not token[0] == ")":
                        self.reculer(1)
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
                    self.reculer(1)
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
                            self.reculer(1)
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
            return True
        
    def verif_stmt_ident(self):
        token = self.lire()
        match token[1]:
            case "ident":
                return self.verif_stmt_type()
            case _:
                self.reculer(1)
                if self.verif_expr_bis():
                    token = self.lire()
                    return(token[0] == ";")
