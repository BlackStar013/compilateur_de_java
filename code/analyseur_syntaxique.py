n = 0

def lire(): #A RETIRER
    return

def reculer():
    return
#################################

def verif_file():
    verif_classes()
    return(verif_class_main())
    

def verif_classes(): #boucle while tant qu'on a un class
    var = True
    while var:
        var = verif_class()
    return


def verif_class():
    token = lire()
    if token[0] == "class":
        token = lire()
        if token[1] == "ident":
            if token[0] == "Main":
                reculer()
                reculer()
                return False
            else:
                token = lire()
                if token[0] == "extends":
                    token = lire()
                    if token[1] != "ident":
                        return False
                    token = lire()
                if token[0] == "{":
                    verif_decles()
                    token = lire()
                    if token[0] == "}":
                        return True
    return("le fichier n'est pas juste")

def verif_decl():
    token = lire()
    match token[0], token[1]:
        case("void",_):
            token = lire()
            if (token[1]=="ident"):
                token = lire()
                if(token[0]=="("):
                    token = lire()
                    if(token[0]!=")"):
                        reculer()
                        if not verif_params():
                            return False
                        token = lire()
                        if token[0] != ")":
                            return False
                    token = lire()
                    if(token[0] == "{"):
                        verif_stmtes()
                        token = lire()
                        if token[0] != "}":
                            return False 
        case("boolean",_):
            return(verif_ident() and verif_decl_suffix())
        case("int",_):
            return(verif_ident() and verif_decl_suffix())
        case (_,"ident"): 
            return(verif_decl_ident())
        case _:
            return False
        
def verif_decles():
    var = True
    while var:
        i = n ####################### N EST LA VARIABLE GLOBALE? FAUDRA VERIFIER QUE C'EST BIEN çA BREF
        var = verif_decl()
    n = i
    


def verif_decl_suffix():
    token = lire()
    match token[0]:
        case ";":
            return True
        case "(":
            token = lire()
            if(token[0]!=")"):
                reculer()
                if not verif_params():
                    return False
                token = lire()
                if token[0] != ")":
                    return False
                token = lire()
            if token[0] == "{":
                verif_stmtes()
                token = lire()
                if token[0] == "}":
                    return True
            return False
        case _ :
            return False
        
#prime devient bis


def verif_lexpr():
    return(verif_expr() and verif_lexpr_bis())


####################################
def verif_lexpr_bis():
    token = lire()
    if token[0] == ",":
        return(verif_lexpr())
    else:
        reculer()
        return True
    
def verif_stmt():
    token = lire()
    match token[0], token[1]:
        case ";", _ : 
            return True
        case "if", _:
            token = lire()
            if token[0] == "(":
                if verif_expr():
                    token = lire()
                    if token[0] == ")":
                        return(verif_stmt() and verif_stmt_if())
        case "for", _:
            token = lire()
            if token[0] == "(":
                for i in range(2):
                    if(token[0] != ";"):
                        reculer()
                        if not verif_expr():
                            return False
                    token = lire()
                    if token[0] != ";":
                        return False
                    token = lire()
                
                if not token[0] == ")":
                    reculer()
                    if not verif_expr():
                        return False
                    token = lire()
                if token[0] == ")":
                    return verif_stmt()
        case "{", _:
            if verif_stmtes():
                token = lire()
                return(token[0] == "}")
        case "return", _:
            token = lire()
            if token[0] != ";":
                reculer()
                if not(verif_expr()):
                    return False
                token = lire()
            if token[0] == ";":
                return True
        case "boolean" | "int", _:
            return(verif_ident() and verif_stmt_type())
        case _,"integer":
            if verif_integer():
                if verif_expr_bis():
                    token = lire()
                    return(token[0] )== ";"
        case _, "mot":
            if verif_string():
                if verif_expr_bis():
                    token = lire()
                    return(token[0] )== ";"
        #######################ON POURRAIT LES REGROUPER AVEC UN TRUC EN MODE {token[1]}
        case "true" | "false" | "this " | "new",_:
            if verif_expr_bis():
                token = lire()
                return(token[0] )== ";"
        case "new", _:
            if verif_ident():
                token = lire()
                if token[0] == "(":
                    token = lire()
                    if token[0] != ")":
                        reculer()
                        if not(verif_expr()):
                            return False
                        token = lire()
                    if token[0] == ")":
                        if verif_expr_bis():
                            token = lire()
                            return(token[0] == ";")
        case "!" | "-",_:
            if verif_expr():
                token = lire()
                return(token[0] )== ";"
        case "(", _:
            if(verif_expr_parenthese() and verif_expr_bis):
                token = lire()
                return(token[0] )== ";"
        case _,"ident":
            return(verif_stmt_ident())
    return False


def verif_stmtes():
    var = True
    while var:
        i = n ####################### N EST LA VARIABLE GLOBALE? FAUDRA VERIFIER QUE C'EST BIEN çA BREF
        var = verif_stmt()
    n = i

def verif_stmt_type():
    token = lire()
    match token[0]:
        case ";":
            return True
        case "=":
            if verif_expr():
                token = lire()
                return(token[0] == ";")
    return False



def verif_if():
    token = lire()
    if(token[0] == "else"):
        return verif_stmt()
    else:
        reculer()
        return True
    
def verif_stmt_ident():
    token = lire()
    match token[1]:
        case "ident":
            return verif_stmt_type()
        case _:
            reculer()
            if verif_expr_bis():
                token = lire()
                return(token[0] == ";")