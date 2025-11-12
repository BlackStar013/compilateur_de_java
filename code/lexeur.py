import sys

chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alpha_min = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alpha_maj = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
mots_cles = ["boolean", "class", "else", "extends", "false", "for", "if", "int", "new", "null", "public", "return", "static", "this", "true", "void"]
symbol = [";", "{", "}" ,"(" ,")", "[" , "]", ","]
operat = ["+", "*", "%", "-", "."]


def lexeur(txt):
    file = open(txt,'r')
    c = file.read(1)
    L = []
    while c != "":
        if c in chiffres: #reconnaître entiers  
            multi = 1
            nb = [c]
            while(1):
                c = file.read(1)
                if(c in chiffres):
                    multi = multi * 10
                    nb.append(c)
                elif(c in alpha_maj or c in alpha_min or c == "." or c == ","): #ALPHABET/REEL DANS CHIFFRE
                    return("Erreur")
                else:
                    nombre = 0
                    for i in range(len(nb)):
                        nombre += multi * int(nb[i])
                        multi = multi/10 
                    L.append((int(nombre), "integer"))
                    break
        elif c in alpha_min or c in alpha_maj or c == "_": #reconnaître un mot clé ou un identifiant
            mot = c
            c =  file.read(1)
            while c in alpha_min or c in alpha_maj or c == '_' or c in chiffres: 
                mot = mot + c
                c = file.read(1)
            if(c not in chiffres and c not in alpha_maj and c not in alpha_min and c != "_" and c != ' ' and c != "\n" and c not in symbol and c not in operat): #CARACTERE NON VOULU DANS ALPHABET
                return("Erreur")
            elif c in chiffres or c == "_":
                while c in alpha_min or c in alpha_maj or c in chiffres or c =="_":
                    mot = mot + c
                    c = file.read(1)
                L.append((mot, "ident"))
            else:
                if mot == "instanceof" or mot == "cast":
                    L.append((mot, "opérateurs"))
                elif mot in mots_cles:
                    L.append((mot, "mots clés"))
                else:
                    L.append((mot, "ident"))
        elif(c == '"'): # pour reconnaître un string
            word = ""
            while(1):
                c = file.read(1)
                if(c == '"'):
                    L.append((word, "mot"))
                    c = file.read(1)
                    break
                else:
                    word = word + c
        elif(c == "/"):  # pour reconnaitre soit la division, soit un commentaire entier, soit un commentaire imbriqué
            c = file.read(1)
            if(c == "/"):
                file.readline()
                c = file.read(1)
            elif(c == "*"):
                c = file.read(1)
                while(1):
                    if(c == "*"):
                        c = file.read(1)
                        if(c == "/"):
                            c = file.read(1)
                            break
                    else:
                        c = file.read(1)
            else:
                L.append(("/", "opérateurs"))
        elif c in symbol: #reconnnaître un symbole simple
            L.append((c, "symboles"))
            c = file.read(1)
        elif c == "|": #reconnaître ||
            c = file.read(1)
            if c != "|":
                return("Erreur")
            else:
                L.append(("||", "opérateurs"))
                c = file.read(1)
        elif c == "&": #reconnaître &&
            c = file.read(1)
            if c != "&":
                return("Erreur")
            else:
                L.append(("&&", "opérateurs"))
                c = file.read(1)
        elif c == "!": #reconnaître ! ou !=
            c = file.read(1)
            if c == "=":
                L.append(("!=", "opérateurs"))
                c = file.read(1)
            else:
                L.append(("!", "opérateurs"))
        elif c == "=": #reconnaître = ou ==
            c = file.read(1)
            if c == "=":
                L.append(("==", "opérateurs"))
                c = file.read(1)
            else:
                L.append(("=", "opérateurs"))
        elif c == "<": #reconnaître < ou <=
            c = file.read(1)
            if c == "=":
                L.append(("<=", "opérateurs"))
                c = file.read(1)
            else:
                L.append(("<", "opérateurs"))
        elif c == ">": #reconnaître > ou >=
            c = file.read(1)
            if c == "=":
                L.append((">=", "opérateurs"))
                c = file.read(1)
            else:
                L.append((">", "opérateurs"))
        elif c in operat: #reconnaître un opérateur simple
            L.append((c, "opérateurs"))
            c = file.read(1)
        elif c == "\n" or c == ' ':
            c = file.read(1)
        else:
            return("Erreur")
    file.close()
    print(L)
    return(L)


def lire(M):
    for i in range(len(M)):
        print(M[i])

def main():
    fichier = sys.argv[1]
    L = lexeur(fichier)
    #lire(L)




if __name__ == "__main__":
    main()
