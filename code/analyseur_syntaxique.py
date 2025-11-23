n = 0

def lire(): #A RETIRER
    return

def reculer():
    return
#################################

def verif_file():
    # mot = lire()
    return(verif_classes() and verif_class_main()) #il y a plusieurs class
    

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
                    if verif_decles():
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
                        if(not verif_params()):
                            return False
                        token = lire()
                        if(token[0] != ")"):
                            return False
                    token = lire()
                    if(token[0] == "{"):
                        token = lire()
                        if(token[0]!="}"):
                            reculer()
                            if not verif_stmtes():
                                return False
                            token = lire()
                            if token[0] != "}":
                                return False
        case("boolean",_):
            token = lire()
            if(token[1] == "ident"):
                return verif_decl_suffix()
            return False
        case("int",_):
            token = lire()
            if(token[1] == "ident"):
                return verif_decl_suffix()
        case (_,"ident"): 
            return(verif_decl_ident())
        case _:
            return False


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
            if token == "{":
                verif_stmtes()
                token = lire()
                if token[0] == "}":
                    return True
            return False
        case _ :
            return False
        
#prime devient bis

def verif_decl_ident():
    token = lire()
    if(token[1] == "ident"):
        return verif_decl_suffix()
    elif(token[0] == "("):
        token = lire()
        if(token[0] != ")"):
            reculer()
            if(not verif_params()):
                return False
            token = lire()
            if(token[0] != ")"):
                return False
            token = lire()
            if(token[0] == "{"):
                token = lire()
                if(token[0]!="}"):
                    reculer()
                    if not verif_stmtes():
                        return False
                    token = lire()
                    if token[0] != "}":
                        return False

def verif_params():
    if(verif_type()):
        token = lire()
        if(token[1] == "ident"):
            return verif_params_bis()

def verif_params_bis():
    token = lire()
    if(token[0] == ","):
        return verif_params()
    return True

def verif_type():
    token = lire()
    if(token[1] == "boolean" or token[1] == "int" or token[1] == "ident"):
        return True
    return False

def verif_class_Main():
    token = lire()
    if(token[1] == "class"):
        token = lire()
        if(token[0] == "Main"):
            token = lire()
            if(token[0] == "{"):
                token = lire()
                if(token[1] == "public"):
                    token = lire()
                    if(token[1] == "static"):
                        token = lire()
                        if(token[1] == "void"):
                            token = lire()
                            if(token[0] == "main"):
                                token = lire()
                                if(token[0] == "("):
                                    token = lire()
                                    if(token[0] == "String"):
                                        token = lire()
                                        if(token[1] == "ident"):
                                            token = lire()
                                            if(token[0] == "["):
                                                token = lire()
                                                if(token[0] == "]"):
                                                    token = lire()
                                                    if(token[0] == ")"):
                                                        token = lire()
                                                        if(token[0] == "{"):
                                                            token = lire()
                                                            if(token[0]!="}"):
                                                                reculer()
                                                                if not verif_stmtes():
                                                                    return False
                                                                token = lire()
                                                                if token[0] != "}":
                                                                    return False
                                                                token = lire()
                                                                if(token[0] == "}"):
                                                                    return True
    return False
