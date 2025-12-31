n = 0


class Parseur:

    correct = True
    nb_erreurs = 0


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
            self.token = ('EOF', 'EOF', self.tokens[self.pos - 1][2])

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
    def erreur(self, token_attendu, ligne):
        self.nb_erreurs += 1
        self.correct = False
        #print("Erreur :", token_attendu,  "est attendu ligne", ligne)

    def verif_file(self):
        #print("passage verif_file")
        # print(self.token)
        self.verif_classes()
        self.verif_class_Main()
        return(self.correct)


    def verif_classes(self): #boucle while tant qu'on a un class
        #print("passage verif_classes")
        var = True
        n = self.nb_erreurs
        while var:
            actuel = self.correct
            i = self.pos
            self.verif_class()
            if(n != self.nb_erreurs):
                var = False
                self.correct = actuel
        self.pos = i
        self.nb_erreurs = n
        return True


    def verif_class(self):
        #print("passage verif_class")
        token = self.lire()
        if token[0] != "class":
            self.erreur("class", token[2])
        token = self.lire()
        if token[1] != "ident":
            self.erreur("ident", token[2])
        if token[0] == "Main":
            token = self.reculer(2)
            self.correct =  False
            self.nb_erreurs += 1
            return
        else:
            token = self.lire()
            if token[0] == "extends":
                token = self.lire()
                if token[1] != "ident":
                    self.erreur("ident", token[2])
                token = self.lire()
            if token[0] != "{":
                self.erreur("{", token[2])
            if self.verif_decles():
                token = self.lire()
                if token[0] != "}":
                    self.erreur("}", token[2])
            else:
                token = self.lire()
                if token != "}":
                    self.erreur("}", token[2])
        return

    def verif_decl(self):
        #print("passage verif_decl")
        token = self.lire()
        match token[0], token[1]:
            case("void",_):
                token = self.lire()
                if (token[1] != "ident"):
                    self.erreur("ident", token[2])
                token = self.lire()
                if(token[0] != "("):
                    self.erreur("(", token[2])
                token = self.lire()
                if(token[0] != ")"):
                    token = self.reculer(1)
                    self.verif_params()                     
                    token = self.lire()
                    if(token[0] != ")"):
                        self.erreur(")", token[2])
                        return 
                token = self.lire()
                if(token[0] != "{"):
                    self.erreur("{", token[2])
                token = self.lire()
                if(token[0] != "}"):
                    token = self.reculer(1)
                    self.verif_stmtes()
                token = self.lire()
                if token[0] != "}":
                    self.erreur("}", token[2])
                    return 
                return 
            case("boolean",_):
                token = self.lire()
                if(token[1] != "ident"):
                    self.erreur("ident", token[2])
                self.verif_decl_suffix()
                return
            case("int",_):
                token = self.lire()
                if(token[1] != "ident"):
                    self.erreur("ident", token[2])
                self.verif_decl_suffix()
            case (_,"ident"): 
                self.verif_decl_ident()
                return
            case _:
                self.correct = False
                self.nb_erreurs += 1
                # self.erreur("decl", token[2])
                return 

    def verif_decles(self):
        #print("passage verif_decles")
        var = True
        n = self.nb_erreurs
        while var:
            actuel = self.correct
            i = self.pos
            self.verif_decl() 
            if n != self.nb_erreurs:
                var = False
                self.correct = actuel
        self.pos = i
        self.nb_erreurs = n
        return True


    def verif_decl_suffix(self):
        #print("passage verif_decl_suffix")
        token = self.lire()
        match token[0]:
            case ";":
                self.correct = self.correct and True
            case "(":
                token = self.lire()
                if(token[0]!=")"):
                    token = self.reculer(1)
                    self.verif_params()
                    token = self.lire()
                    if token[0] != ")":
                        self.erreur(")", token[2])
                    token = self.lire()
                if token == "{":
                    self.verif_stmtes()
                    token = self.lire()
                    if token[0] != "}":
                        self.erreur("}", token[2])
                    else:
                        self.correct = self.correct and True
            case _ :
                self.erreur("; ou (", token[2])
        return

    #prime devient bis

    def verif_decl_ident(self):
        #print("passage verif_decl_ident")
        token = self.lire()
        if(token[1] == "ident"):
            self.verif_decl_suffix()
        elif(token[0] == "("):
            token = self.lire()
            if(token[0] != ")"):
                token = self.reculer(1)
                if(not self.verif_params()):
                    return
                token = self.lire()
                if(token[0] != ")"):
                    self.erreur(")", token[2])
                    return
                token = self.lire()
                if(token[0] != "{"):
                    self.erreur("{", token[2])
                token = self.lire()
                if(token[0]!="}"):
                    token = self.reculer(1)
                    if not self.verif_stmtes():
                        return
                    token = self.lire()
                    if token[0] != "}":
                        self.erreur("}", token[2])
                        return 

    def verif_params(self):
        #print("passage verif_params")
        self.verif_type()
        token = self.lire()
        if(token[1] != "ident"):
            self.erreur("ident", token[2])
        self.verif_params_bis()
        return 

    def verif_params_bis(self):
        #print("passage verif_params_bis")
        token = self.lire()
        if(token[0] == ","):
            self.verif_params()
        else:
            self.reculer(1)
        self.correct = self.correct and True
        return

    def verif_type(self):
        #print("passage verif_type")
        token = self.lire()

        if(token[0] == "boolean" or token[0] == "int" or token[1] == "ident"):
            self.correct = self.correct and True
            return 
        self.erreur("boolean ou int ou un ident", token[2])
        return 

    def verif_class_Main(self):
        #print("passage verif_class_Main")
        token = self.lire()
        if(token[0] != "class"):
            self.erreur("class", token[2])
        token = self.lire()
        if(token[0] != "Main"):
            self.erreur("Main", token[2])
        token = self.lire()
        if(token[0] != "{"):
            self.erreur("{", token[2])
        token = self.lire()
        if(token[0] != "public"):
            self.erreur("public", token[2])
        token = self.lire()
        if(token[0] != "static"):
            self.erreur("static", token[2])
        token = self.lire()
        if(token[0] != "void"):
            self.erreur("void", token[2])
        token = self.lire()
        if(token[0] != "main"):
            self.erreur("main", token[2])
        token = self.lire()
        if(token[0] != "("):
            self.erreur("(", token[2])
        token = self.lire()
        if(token[0] != "String"):
            self.erreur("String", token[2])
        token = self.lire()
        if(token[1] != "ident"):
            self.erreur("ident", token[2])
        token = self.lire()
        if(token[0] != "["):
            self.erreur("[", token[2])
        token = self.lire()
        if(token[0] != "]"):
            self.erreur("]", token[2])
        token = self.lire()
        if(token[0] != ")"):
            self.erreur(")", token[2])
        token = self.lire()
        if(token[0] != "{"):
            self.erreur("{", token[2])                   
        token = self.lire()
        if(token[0]!="}"):
            token = self.reculer(1)
            if not self.verif_stmtes():
                 return
            token = self.lire()
            if token[0] != "}":
                self.erreur("}", token[2])
                return
            token = self.lire()
            if(token[0] == "}"):
                self.correct = self.correct and True
        elif(token[0] == "}"):
            token = self.lire()
            if(token[0] != "}"):
                self.erreur("}",token[2])
            self.correct = self.correct and True
        return 


    def verif_expr(self) :
        #print("passage verif_expr")
        self.verif_expr_N2()
        self.verif_expr_N1_bis()
        return
    
    def verif_expr_N1_bis(self) :
        #print("passage verif_expr_N1_bis")
        token = self.lire()
        if token[0] != '=' :
            self.reculer(1)
            return
        self.verif_expr()
        return
        
    def verif_expr_N2(self) :
        #print("passage verif_expr_N2")
        self.verif_expr_N3()
        self.verif_expr_N2_bis()
        return
    
    def verif_expr_N2_bis(self) :
        #print("passage verif_expr_N2_bis")
        token = self.lire()
        if token[0] == '||' :
            self.verif_expr_N3()
            self.verif_expr_N2_bis()
            return
        else :
            token = self.reculer(1)
            return 
     
        
    def verif_expr_N3(self) :
        #print("passage verif_expr_N3")
        self.verif_expr_N4()
        self.verif_expr_N3_bis()
        return 
    
    def verif_expr_N3_bis(self) :
        #print("passage verif_expr_N3_bis")
        token = self.lire()
        if token[0] == '&&' :
            self.verif_expr_N4()
            self.verif_expr_N3_bis() 
        else :
            token = self.reculer(1)
        return 
        
    def verif_expr_N4(self) :
        #print("passage verif_expr_N4")
        self.verif_expr_N5()
        self.verif_expr_N4_bis()
        return
    
    def verif_expr_N4_bis(self) :
        #print("passage verif_expr_N4_bis")
        token = self.lire()
        match token[0] :
            case "==" :
                self.verif_expr_N5()
                self.verif_expr_N4_bis()
                return
            case "!=" :
                self.verif_expr_N5()
                self.verif_expr_N4_bis()
                return
            case _ :
                token = self.reculer(1)
                return 
            
    def verif_expr_N5(self) :
        #print("passage verif_expr_N5")
        self.verif_expr_N6()
        self.verif_expr_N5_bis()
        return
    
    def verif_expr_N5_bis(self) :
        #print("passage verif_expr_N5_bis")
        token = self.lire()
        match token[0] :
            case "<" :
                self.verif_expr_N6()
                self.verif_expr_N5_bis()
                return
            case "<=" :
                self.verif_expr_N6() 
                self.verif_expr_N5_bis()
                return
            case ">" :
                self.verif_expr_N6()
                self.verif_expr_N5_bis()
                return
            case ">=" :
                self.verif_expr_N6() 
                self.verif_expr_N5_bis()
                return
            case "instanceof" :
                self.verif_type()
                self.verif_expr_N5_bis()
                return
            case _ :
                token = self.reculer(1)
                return True 
            
    def verif_expr_N6(self) :
        #print("passage verif_expr_N6")
        self.verif_expr_N7()
        self.verif_expr_N6_bis()
        return
    
    def verif_expr_N6_bis(self) :
        #print("passage verif_expr_N6_bis")
        token = self.lire()
        match token[0] :
            case "+" :
                self.verif_expr_N7()
                self.verif_expr_N6_bis()
                return 
            case "-" :
                self.verif_expr_N7()
                self.verif_expr_N6_bis()
                return
            case _ :
                token = self.reculer(1)
                return  
    
    def verif_expr_N7(self) :
        #print("passage verif_expr_N7")
        self.verif_expr_N8()
        self.verif_expr_N7_bis()
        return
    
    def verif_expr_N7_bis(self) :
        #print("passage verif_expr_N7_bis")
        token = self.lire()
        match token[0] :
            case "*" :
                self.verif_expr_N8()
                self.verif_expr_N7_bis()
                return 
            case "/" :
                self.verif_expr_N8()
                self.verif_expr_N7_bis()
                return
            case "%" :
                self.verif_expr_N8()
                self.verif_expr_N7_bis()
                return
            case _ :
                token = self.reculer(1)
                return  
            
    def verif_expr_N8(self) :
        #print("passage verif_expr_N8")
        token = self.lire()
        match token[0] :
            case "!" :
                self.verif_expr_N8()
                return
            case "-" :
                self.verif_expr_N8()
                return
            case "(" :
                self.verif_expr_parenthese()
                return
            case _ :
                token = self.reculer(1)
                self.verif_expr_N9()
                return

    def verif_expr_N9(self) :
        #print("passage verif_expr_N9")
        self.verif_item()
        self.verif_expr_N9_bis()
        return 

###########################################################JEN ETAIS A ICI
    def verif_expr_N9_bis(self) :
        #print("passage verif_expr_N9_bis")
        token = self.lire()
        match token[0] :
            case "." :
                token = self.lire()
                if token[1] != "ident" :
                    self.erreur("ident", token[2])
                self.verif_expr_ident()
                return
            case "(" :
                token = self.lire()
                if token[0] != ")" :
                    token = self.reculer(1)
                    self.verif_lexpr()
                    token = self.lire()
                if token[0] != ")" :
                    self.erreur(")", token[2])
                self.verif_expr_N9_bis()
                return 
            case _ :
                token = self.reculer(1)
                return
            
    def verif_expr_ident(self) :
        #print("passage verif_expr_ident")
        token = self.lire()
        if token[0] == '=' :
            self.verif_expr()
            return
        else :
            token = self.reculer(1)
            self.verif_expr_N9_bis()
            return
    
    ############################################################ je reprends a partir de la
    def verif_item(self) :
        #print("passage verif_item")
        token = self.lire()
        match token[0], token[1] :
            case _, "integer" :
                return
            case _, "mot" :
                return 
            case "true", _ :
                return
            case "false", _ :
                return 
            case "this", _ :
                return
            case "null", _ :
                return 
            case "new", _ :
                token = self.lire()
                if token[1] != "ident" :
                    self.erreur("ident", token[2])
                token = self.lire()
                if token[0] != "(" :   
                    self.erreur("(", token[2])
                token = self.lire()
                if token[0] != ")" :
                    token = self.reculer(1)
                    self.verif_lexpr() 
                    token = self.lire()
                    if token[0] != ")" :
                        self.erreur(")", token[2])
                        return 
            case _, "ident" :
                return 
    
    ################################################################"" Arreter ici pour Moi (à savoir moi), à finir
    
   # def verif_expr_parenthese(self) :  cas à compléter 2
    def verif_expr_parenthese(self) : 
        #print("passage verif_parenthese")
        save_pos = self.pos
        token = self.lire()
        maybe_type = False
        if (token[0] in ["boolean", "int"] or token[1] == "ident") :
            maybe_type = True 
        if maybe_type :
            next_token = self.lire() 
            if(next_token == ")"):
                nb = self.nb_erreurs
                self.verif_expr_N8()
                if nb == self.nb_erreurs:
                        return
                else :  # Il faut reculer de l'ensemble des éléments testés dans self.verif_expr_N8
                    self.nb_erreurs = nb
                    new_pos = self.pos
                    self.reculer(new_pos - save_pos - 1)
            else : 
                self.reculer(1)
        self.reculer(1)
        self.verif_expr()
        token = self.lire()
        if token[0] != ")" :
            self.erreur(")", token[2])
        return  

        
    def verif_expr_bis(self) :
        #print("passage verif_expr_bis")
        self.verif_expr_N9_bis()
        self.verif_expr_N7_bis()
        self.verif_expr_N6_bis()
        self.verif_expr_N5_bis()
        self.verif_expr_N4_bis()
        self.verif_expr_N3_bis()
        self.verif_expr_N2_bis()
        self.verif_expr_N1_bis()
        return


    def verif_lexpr(self):
        #print("passage verif_lexpr")
        self.verif_expr()
        self.verif_lexpr_bis()
        return

    def verif_lexpr_bis(self):
        #print("passage verif_lexpr_bis")
        token = self.lire()
        if token[0] == ",":
            self.verif_lexpr()
            return
        else:
            token = self.reculer(1)
            return
        
    def verif_stmt(self):
        #print("passage verif_stmt")
        token = self.lire()
        match token[0], token[1]:
            case ";", _ : 
                return
            case "if", _:
                token = self.lire()
                if token[0] != "(":
                    self.erreur("(", token[2])
                self.verif_expr()
                token = self.lire()
                if token[0] != ")":
                    self.erreur(")", token[2])
                self.verif_stmt()
                self.verif_stmt_if()
                return
            case "for", _:
                token = self.lire()
                if token[0] != "(":
                    self.erreur("(", token[2])
                for i in range(2):
                    if(token[0] != ";"):
                        token = self.reculer(1)
                        self.verif_expr()
                    token = self.lire()
                    if token[0] != ";":
                        self.erreur(";", token[2])
                    token = self.lire()
                
                if not token[0] == ")":
                    token = self.reculer(1)
                    self.verif_expr()
                    token = self.lire()
                if token[0] == ")":
                    self.verif_stmt()
                return
            case "{", _:
                self.verif_stmtes()
                token = self.lire()
                if(token[0] != "}"):
                    self.erreur("}", token[2])
                return
            case "return", _:
                token = self.lire()
                if token[0] != ";":
                    token = self.reculer(1)
                    self.verif_expr()
                    token = self.lire()
                if token[0] != ";":
                    self.erreur(";", token[2])
                return
            case "boolean" | "int", _:
                token = self.lire()
                if(token[1] != "ident"):
                    self.erreur("ident", token[2])
                self.verif_stmt_type()
                return
            case _,"integer":
                self.verif_expr_bis()
                token = self.lire()
                if(token[2] != ";"):
                    self.erreur(";", token[2])
                return
            case _, "mot":
                self.verif_expr_bis()
                token = self.lire()
                if(token[0] != ";"):
                    self.erreur(";", token[2])
                return
            #######################ON POURRAIT LES REGROUPER AVEC UN TRUC EN MODE {token[1]}
            case "true" | "false" | "this" | "new",_:
                self.verif_expr_bis()
                token = self.lire()
                if(token[0] != ";"):
                    self.erreur(";", token[2])
                return
            case "new", _:
                token = self.lire()
                if(token[0] != "ident"):
                    self.erreur("ident", token[2])
                token = self.lire()
                if token[0] != "(":
                    self.erreur("(", token[2])
                token = self.lire()
                if token[0] != ")":
                    token = self.reculer(1)
                    self.verif_expr()
                    token = self.lire()
                if token[0] != ")":
                    self.erreur(")", token[2])
                self.verif_expr_bis()
                token = self.lire()
                if(token[0] != ";"):
                    self.erreur(";", token[2])
                return
            case "!" | "-",_:
                self.verif_expr()
                token = self.lire()
                if(token[0] != ";"):
                    self.erreur(";", token[2])
                return
            case "(", _:
                self.verif_expr_parenthese()
                self.verif_expr_bis()
                token = self.lire()
                if(token[0] != ";"):
                    self.erreur(";", token[2])
                return
            case _,"ident":
                self.verif_stmt_ident()
                return
        self.correct = False
        self.nb_erreurs += 1
        # self.erreur("statement", token[2])
        return


    def verif_stmtes(self):
        #print("passage verif_stmtes")
        var = True
        n = self.nb_erreurs
        while var:
            actuel = self.correct
            i = self.pos ####################### N EST LA VARIABLE GLOBALE? FAUDRA VERIFIER QUE C'EST BIEN çA BREF
            self.verif_stmt()
            if(n != self.nb_erreurs):
                var = False
                self.correct = actuel
        self.pos = i
        self.nb_erreurs = n
        return True

    def verif_stmt_type(self):
        #print("passage verif_stmt_type")
        token = self.lire()
        match token[0]:
            case ";":
                return
            case "=":
                self.verif_expr()
                token = self.lire()
                if(token[0] != ";"):
                    self.erreur(";", token[2])
                return
        self.correct = False
        self.nb_erreurs += 1
        # self.erreur("statement type", token[2])
        return



    def verif_stmt_if(self):
        #print("passage verif_if")
        token = self.lire()
        if(token[0] == "else"):
            self.verif_stmt()
            return
        else:
            token = self.reculer(1)
            return 
        
    def verif_stmt_ident(self):
        #print("passage verif_stmt_ident")
        token = self.lire()
        match token[1]:
            case "ident":
                self.verif_stmt_type()
                return
            case _:
                token = self.reculer(1)
                self.verif_expr_bis()
                token = self.lire()
                if(token[0] != ";"):
                    self.erreur(";", token[2])
                return
