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
