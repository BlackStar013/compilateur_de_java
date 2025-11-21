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
                        if not verif_params():
                            return False
                        token = lire()
                        if token[0] != ")":
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
            return(verif_ident() and verif_decl_suffix())
        case("int",_):
            return(verif_ident() and verif_decl_suffix())
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