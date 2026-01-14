from nodes_class import *
class Parseur():

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = -1
        self.token = tokens[self.pos]
        self.correct = True
        self.nb_erreurs = 0

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
        class_l = self.verif_classes()
        main = self.verif_class_Main()
        return File(main, class_l)


    def verif_classes(self): #boucle while tant qu'on a un class
        #print("passage verif_classes")
        var = True
        n = self.nb_erreurs
        class_l = []
        while var:
            actuel = self.correct
            i = self.pos
            cl = self.verif_class()
            if(n != self.nb_erreurs):
                var = False
                self.correct = actuel
            if cl is not None:
                class_l.append(cl)
        self.pos = i
        self.nb_erreurs = n
        # retroune les classes trouvées
        return class_l


    def verif_class(self):
        #print("passage verif_class")
        token = self.lire()
        if token[0] != "class":
            self.erreur("class", token[2])
        token = self.lire()
        nom_class = token[0]
        if token[1] != "ident":
            self.erreur("ident", token[2])
        if token[0] == "Main":
            token = self.reculer(2)
            self.correct =  False
            self.nb_erreurs += 1
            return None
        else:
            token = self.lire()
            ext = None
            if token[0] == "extends":
                token = self.lire()
                if token[1] != "ident":
                    self.erreur("ident", token[2])
                ext = token[0]
                token = self.lire()
            if token[0] != "{":
                self.erreur("{", token[2])
            declB = self.verif_decles()
            token = self.lire()
            if token[0] != "}":
                self.erreur("}", token[2])
        return Class(nom_class, declB, ext)

    def verif_decl(self):
        #print("passage verif_decl")
        token = self.lire()
        match token[0], token[1]:
            case("void",_):
                token = self.lire()
                nom_methode = token[0]
                if (token[1] != "ident"):
                    self.erreur("ident", token[2])
                token = self.lire()
                if(token[0] != "("):
                    self.erreur("(", token[2])
                token = self.lire()

                noeud_paramB = None

                if(token[0] != ")"):
                    token = self.reculer(1)
                    param_l = self.verif_params()
                    noeud_paramB = ParamBlock(param_l)                     
                    token = self.lire()
                    if(token[0] != ")"):
                        self.erreur(")", token[2])
                        return 
                token = self.lire()
                if(token[0] != "{"):
                    self.erreur("{", token[2])
                token = self.lire()

                noeud_stmtB = None

                if(token[0] != "}"):
                    token = self.reculer(1)
                    noeud_stmtB = self.verif_stmtes()
                token = self.lire()
                if token[0] != "}":
                    self.erreur("}", token[2])
                    return 
                return Methode(nom_methode, "void", noeud_stmtB, noeud_paramB)
            case("boolean",_):
                token = self.lire()
                nom = token[0]
                if(token[1] != "ident"):
                    self.erreur("ident", token[2])

                nds = self.verif_decl_suffix()
                if nds[0] == "Methode":
                    return Methode(nom, "boolean", nds[2], nds[1])
                elif nds[0] == "Attribut":
                    return Champ("boolean", nom)
                return 
            
            case("int",_):
                token = self.lire()
                nom = token[0]
                if(token[1] != "ident"):
                    self.erreur("ident", token[2])

                nds = self.verif_decl_suffix()
                if nds[0] == "Methode":
                    return Methode(nom, "int", nds[2], nds[1])
                elif nds[0] == "Attribut":
                    return Champ("int", nom)
                return
            
            case (_,"ident"):
                ret_type = token[0] 
                nds = self.verif_decl_ident()
                if nds[0] == "Methode":
                    return Methode(nds[-1], ret_type , nds[2], nds[1])
                elif nds[0] == "Const":
                    return Constructeur(ret_type, nds[2], nds[1])
                elif nds[0] == "Attribut":
                    return Champ(ret_type, nds[-1])
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
        decl_l = []
        while var:
            actuel = self.correct
            i = self.pos
            decl = self.verif_decl() 
            if n != self.nb_erreurs:
                var = False
                self.correct = actuel
            if decl is not None:
                decl_l.append(decl)
        self.pos = i
        self.nb_erreurs = n
        return DeclBlock(decl_l)


    def verif_decl_suffix(self):
        #print("passage verif_decl_suffix")
        token = self.lire()
        match token[0]:
            case ";":
                self.correct = self.correct and True
                return "Attribut", None, None
            case "(":
                token = self.lire()
                noeud_paramB = None
                if(token[0]!=")"):
                    token = self.reculer(1)
                    param_l = self.verif_params()
                    noeud_paramB = ParamBlock(param_l) 
                    token = self.lire()
                    if token[0] != ")":
                        self.erreur(")", token[2])
                    token = self.lire()
                    noeud_stmtB = None
                if token[0] == "{":
                    noeud_stmtB = self.verif_stmtes()
                    token = self.lire()
                    if token[0] != "}":
                        self.erreur("}", token[2])
                    else:
                        self.correct = self.correct and True
                        return "Methode", noeud_paramB, noeud_stmtB
            case _ :
                self.erreur("; ou (", token[2])
        return None, None, None

    #prime devient bis

    def verif_decl_ident(self):
        #print("passage verif_decl_ident")
        token = self.lire()
        if(token[1] == "ident"):
            nom = token[0]
            nds_suf = self.verif_decl_suffix()
            return nds_suf, nom
        elif(token[0] == "("):
            token = self.lire()
            paramB = None
            if(token[0] != ")"):
                token = self.reculer(1)

                param_l = self.verif_params()
                paramB = ParamBlock(param_l)

                token = self.lire()
                if(token[0] != ")"):
                    self.erreur(")", token[2])
                
                token = self.lire()
                if(token[0] != "{"):
                    self.erreur("{", token[2])

                stmtB = self.verif_stmtes()
                token = self.lire()

                if(token[0]!="}"):
                    self.erreur("}", token[2])

                return "Const", paramB, stmtB, None
        else:    
            self.erreur("ident ou (", token[2])
            return None, None, None, None

    def verif_params(self):
        #print("passage verif_params")
        type_param = self.verif_type()
        token = self.lire()
        if(token[1] != "ident"):
            self.erreur("ident", token[2])

        nom_param = token
        noeud_param = Param(type_param, nom_param)

        suite_param = self.verif_params_bis()
        return [noeud_param] + suite_param

    def verif_params_bis(self):
        #print("passage verif_params_bis")
        param_l = []
        token = self.lire()
        if(token[0] == ","):
            param_l = self.verif_params()
        else:
            self.reculer(1)
        self.correct = self.correct and True
        return param_l

    def verif_type(self):
        #print("passage verif_type")
        token = self.lire()

        if(token[0] == "boolean" or token[0] == "int" or token[1] == "ident"):
            self.correct = self.correct and True
            return token[0]
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
        nom_arg = token[0]
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
    
        noeud_stmt_block = self.verif_stmtes()
        token = self.lire()
        
        if(token[0]!="}"):
            self.erreur("}", token[2])
            token = self.lire()
            if token[0] != "}":
                self.erreur("}", token[2])
                return
            if(token[0] == "}"):
                self.correct = self.correct and True
        elif(token[0] == "}"):
            token = self.lire()
            if(token[0] != "}"):
                self.erreur("}",token[2])
            self.correct = self.correct and True
        return  Class_Main(nom_arg, noeud_stmt_block)


    def verif_expr(self) :
        #print("passage verif_expr")
        gauche = self.verif_expr_N2()
        return self.verif_expr_N1_bis(gauche)
    
    def verif_expr_N1_bis(self, g) :
        #print("passage verif_expr_N1_bis")
        token = self.lire()
        if token[0] != '=' :
            self.reculer(1)
            return g
        d = self.verif_expr()
        return Attribution(g, d)
        
    def verif_expr_N2(self) :
        #print("passage verif_expr_N2")
        g = self.verif_expr_N3()
        return self.verif_expr_N2_bis(g)
    
    def verif_expr_N2_bis(self, g) :
        #print("passage verif_expr_N2_bis")
        token = self.lire()
        op = token[0]
        if op == '||' :
            d = self.verif_expr_N3()
            n = Binop(op, g, d)
            return self.verif_expr_N2_bis(n)
        else :
            token = self.reculer(1)
            return g
        
    def verif_expr_N3(self) :
        #print("passage verif_expr_N3")
        g = self.verif_expr_N4()
        return self.verif_expr_N3_bis(g) 
    
    def verif_expr_N3_bis(self, g) :
        #print("passage verif_expr_N3_bis")
        token = self.lire()
        op = token[0]
        if op == '&&' :
            d = self.verif_expr_N4()
            n = Binop(op, g, d)
            return self.verif_expr_N3_bis(n) 
        else :
            token = self.reculer(1)
            return g
        
    def verif_expr_N4(self) :
        #print("passage verif_expr_N4")
        g = self.verif_expr_N5()
        return self.verif_expr_N4_bis(g)
    
    def verif_expr_N4_bis(self, g) :
        #print("passage verif_expr_N4_bis")
        token = self.lire()
        op = token[0]
        match op :
            case "==" | "!=" :
                d = self.verif_expr_N5()
                n = Binop(op, g, d)
                return self.verif_expr_N4_bis(n)
            case _ :
                token = self.reculer(1)
                return g
            
    def verif_expr_N5(self) :
        #print("passage verif_expr_N5")
        g = self.verif_expr_N6()
        return self.verif_expr_N5_bis(g)
    
    def verif_expr_N5_bis(self, g) :
        #print("passage verif_expr_N5_bis")
        token = self.lire()
        op = token[0]
        match op :
            case "<" | "<=" | ">" | ">=" :
                d = self.verif_expr_N6()
                noeud = Binop(op, g, d)
                return self.verif_expr_N5_bis(noeud)
            case "instanceof" :
                cible_type = self.verif_type()
                noeud = Instanceof(cible_type, g)
                return self.verif_expr_N5_bis(noeud)
            case _ :
                token = self.reculer(1)
                return g 
            
    def verif_expr_N6(self) :
        #print("passage verif_expr_N6")
        g = self.verif_expr_N7()
        return self.verif_expr_N6_bis(g)
    
    def verif_expr_N6_bis(self, g) :
        #print("passage verif_expr_N6_bis")
        token = self.lire()
        op = token[0]
        match op :
            case "+" | "-" :
                d = self.verif_expr_N7()
                n = Binop(op, g, d)
                return self.verif_expr_N6_bis(n) 
            case _ :
                token = self.reculer(1)
                return g
    
    def verif_expr_N7(self) :
        #print("passage verif_expr_N7")
        g = self.verif_expr_N8()
        return self.verif_expr_N7_bis(g)
    
    def verif_expr_N7_bis(self, g) :
        #print("passage verif_expr_N7_bis")
        token = self.lire()
        op = token[0]
        match op :
            case "*" | "/" | "%":
                d = self.verif_expr_N8()
                n = Binop(op, d, g)
                return self.verif_expr_N7_bis(n)
            case _ :
                token = self.reculer(1)
                return g  
            
    def verif_expr_N8(self) :
        #print("passage verif_expr_N8")
        token = self.lire()
        op = token[0]
        match op :
            case "!" | "-"  :
                exp = self.verif_expr_N8()
                return Unop(op, exp)
            case "(" :
                return self.verif_expr_parenthese()
            case _ :
                token = self.reculer(1)
                return self.verif_expr_N9()

    def verif_expr_N9(self) :
        #print("passage verif_expr_N9")
        g = self.verif_item()
        return self.verif_expr_N9_bis(g) 

###########################################################JEN ETAIS A ICI
    def verif_expr_N9_bis(self, g) :
        #print("passage verif_expr_N9_bis")
        token = self.lire()
        match token[0] :
            case "." :
                token = self.lire()
                if token[1] != "ident" :
                    self.erreur("ident", token[2])
                nom_champ = token[0]
                n_g = AccesChamp(g, nom_champ)
                return self.verif_expr_N9_bis(n_g)
            case "(" :
                nom_funct = "inconnu"
                obj = None
                if isinstance(g, Element) and g.fils[0].nom is None:
                     nom_funct = g.fils[1].name
                     obj = Node("this")
                elif isinstance(g, AccesChamp):
                     # AccesChamp -> fils[0]=obj, fils[1]=nom_champ
                     obj = g.fils[0]
                     nom_funct = g.fils[1].name
                else:
                    obj = g

                token = self.lire()
                args = []
                if token[0] != ")" :
                    token = self.reculer(1)
                    args = self.verif_lexpr()
                    token = self.lire()
                if token[0] != ")" :
                    self.erreur(")", token[2])
                n_g = AppelMethode(obj, nom_funct, args)
                return self.verif_expr_N9_bis(n_g) 
            case _ :
                token = self.reculer(1)
                return g
            
    def verif_expr_ident(self) :
        #print("passage verif_expr_ident")
        token = self.lire()
        n = Element(None, token[0])
        if token[0] == '=' :
            d = self.verif_expr()
            return Attribution(n,d)
        else :
            token = self.reculer(1)
            expr = self.verif_expr_N9_bis(n)
            return expr
    
    ############################################################ je reprends a partir de la
    def verif_item(self) :
        #print("passage verif_item")
        token = self.lire()
        match token[0], token[1] :
            case _, "integer" :
                ret_type = "integer" 
            case _, "mot" :
                ret_type = "String"
            case "true", _ :
                ret_type = "boolean"
            case "false", _ :
                ret_type = "boolean" 
            case "this", _ :
                ret_type = "this"
            case "null", _ :
                ret_type = "null" 
            case "new", _ :
                token = self.lire()
                nom = token[0]
                if token[1] != "ident" :
                    self.erreur("ident", token[2])
                token = self.lire()
                if token[0] != "(" :   
                    self.erreur("(", token[2])
                token = self.lire()
                args_l = []
                if token[0] != ")" :
                    token = self.reculer(1)
                    args_l = self.verif_lexpr() 
                    token = self.lire()
                    if token[0] != ")" :
                        self.erreur(")", token[2])
                        return               
                return New(nom, args_l)
            
            case _, "ident" :
                ret_type = None
        return Element(ret_type,token[0])
    
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
            cible_type = token[0]
            next_token = self.lire() 
            if(next_token == ")"):
                nb = self.nb_erreurs
                exp = self.verif_expr_N8()
                if nb == self.nb_erreurs:
                        return Cast(cible_type, exp)
                else :  # Il faut reculer de l'ensemble des éléments testés dans self.verif_expr_N8
                    self.nb_erreurs = nb
                    new_pos = self.pos
                    self.reculer(new_pos - save_pos - 1)
            else : 
                self.reculer(1)
        self.reculer(1)
        exp = self.verif_expr()
        token = self.lire()
        if token[0] != ")" :
            self.erreur(")", token[2])
        return exp

        
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
        exp = self.verif_expr()
        suite = self.verif_lexpr_bis()
        return [exp] + suite

    def verif_lexpr_bis(self):
        #print("passage verif_lexpr_bis")
        token = self.lire()
        if token[0] == ",":
            return self.verif_lexpr()
        else:
            self.reculer(1)
            return []
        
    def verif_stmt(self):
        #print("passage verif_stmt")
        token = self.lire()
        match token[0], token[1]:
            case ";", _ : 
                return Node("_")
            case "if", _:
                token = self.lire()
                if token[0] != "(":
                    self.erreur("(", token[2])
                expr = self.verif_expr()
                token = self.lire()
                if token[0] != ")":
                    self.erreur(")", token[2])
                n_stmt = self.verif_stmt()
                n_if = self.verif_stmt_if()
                return If(expr, n_stmt, n_if)
            
            case "for", _:
                token = self.lire()
                if token[0] != "(":
                    self.erreur("(", token[2])
                
                token = self.lire()
                init = Node("_")
                if(token[0] != ";"):
                    token = self.reculer(1)
                    init = self.verif_expr()
                    token = self.lire()
                if token[0] != ";":
                    self.erreur(";", token[2])
                
                token = self.lire()
                cond = Node("_")
                if(token[0] != ";"):
                    token = self.reculer(1)
                    incondit = self.verif_expr()
                    token = self.lire()
                if token[0] != ";":
                    self.erreur(";", token[2])
                
                token = self.lire()
                maj = Node("_")
                if(token[0] != ")"):
                    token = self.reculer(1)
                    maj = self.verif_expr()
                    token = self.lire()
                if token[0] != ")":
                    self.erreur(")", token[2])
                
                n_stmt = self.verif_stmt()
                return For(init, cond, maj, StmtBlock(n_stmt))
            
            case "{", _:
                n_stmtB = self.verif_stmtes()
                token = self.lire()
                if(token[0] != "}"):
                    self.erreur("}", token[2])
                return n_stmtB
            
            case "return", _:
                expr = None
                token = self.lire()
                if token[0] != ";":
                    token = self.reculer(1)
                    expr = self.verif_expr()
                    token = self.lire()
                if token[0] != ";":
                    self.erreur(";", token[2])
                return Return(expr)
            
            case "boolean" | "int", _:
                ret_type = token[0]
                token = self.lire()
                nom = token[0]
                if(token[1] != "ident"):
                    self.erreur("ident", token[2])

                nds = self.verif_stmt_type()
                if nds[0] == "Init":
                    expr_init = nds[1] 
                else: expr_init = None
                return ExprVar(ret_type, nom, expr_init)
            
            case _,"integer" | "mot":
                pass
            #######################ON POURRAIT LES REGROUPER AVEC UN TRUC EN MODE {token[1]}
            case "true" | "false" | "this" | "null" ,_:
                pass
            case "new", _:
                pass
            case "!" | "-",_:
                pass
            case "(", _:
                pass
            case _,"ident":
                self.reculer(1)
                return self.verif_stmt_ident()
            case _,_:
                if token[1] in ["integer", "mot"] or token[0] in ["true", "false", "this", "null", "new", "!", "-", "("]:
                    self.reculer(1) # On remet le token pour verif_expr
                    expr = self.verif_expr()
                    
                    token = self.lire()
                    if token[0] != ";":
                        self.erreur(";", token[2])
                    
                    return ExprStmt(expr)
                else:
                    # Vraie erreur syntaxique
                    self.correct = False
                    self.nb_erreurs += 1
                    print("une erreur est détéctée???")
                    return Node("_")


    def verif_stmtes(self):
        #print("passage verif_stmtes")
        var = True
        n = self.nb_erreurs
        stmt_l = []
        while var:
            actuel = self.correct
            i = self.pos ####################### N EST LA VARIABLE GLOBALE? FAUDRA VERIFIER QUE C'EST BIEN çA BREF
            stmt = self.verif_stmt()
            if(n != self.nb_erreurs):
                var = False
                self.correct = actuel
            if stmt is not None:
                stmt_l.append(stmt)
        self.pos = i
        self.nb_erreurs = n
        return StmtBlock(stmt_l)

    def verif_stmt_type(self):
        #print("passage verif_stmt_type")
        token = self.lire()
        match token[0]:
            case ";":
                return "Déclaration", None
            case "=":
                expr = self.verif_expr()
                token = self.lire()
                if(token[0] != ";"):
                    self.erreur(";", token[2])
                return "Init", expr
        self.correct = False
        self.nb_erreurs += 1
        # self.erreur("statement type", token[2])
        return

    def verif_stmt_if(self):
        #print("passage verif_if")
        token = self.lire()
        if(token[0] == "else"):
            stmt = self.verif_stmt()
            return stmt
        else:
            token = self.reculer(1)
            return Node("_")
    '''    
    def verif_stmt_ident(self):
        #print("passage verif_stmt_ident")
        token = self.lire()
        match token[1]:
            case "ident":
                nds = self.verif_stmt_type()
                return nds, token[0]
            case _:
                token = self.reculer(1)
                expr = self.verif_expr_bis()
                token = self.lire()
                if(token[0] != ";"):
                    self.erreur(";", token[2])
                return "Expr", expr
    '''
    def verif_stmt_ident(self):
        type_potentiel = self.token[0] 
        token = self.lire()
        if token[1] == "ident":
            nom_var = token[0]
            token = self.lire()
            expr_init = None
            if token[0] == "=":
                expr_init = self.verif_expr()
                token = self.lire()        
            if token[0] != ";":
                self.erreur(";", token[2])
            return ExprVar(type_potentiel, nom_var, expr_init)
        else:
            # On doit annuler lectures pour utiliser verif_expr()
            # On recule de 2 : 
            #   1. Le token actuel (qui n'était pas un ident)
            #   2. Le token précédent (type_potentiel) qui est le début de l'expression
            self.reculer(2)
            expr = self.verif_expr()
            token = self.lire()
            if token[0] != ";":
                self.erreur(";", token[2])
            return ExprStmt(expr)
