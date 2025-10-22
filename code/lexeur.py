#from re import * #marche pas en tout cas pour l'instant car read lit des str
import sys

chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alpha_min = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alpha_maj = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
operateur = ["+", "-", "*", "/", "%", "=", "||", "&&", "!=", "<", "<=", ">=", ">", "."]
symbole = [",", ";", "(", ")", "[", "]", "{", "}"]

#print("au revoir", len(sys.argv))
#print("bonjour", sys.argv[1])
def lexeur():
    file = open(sys.argv[1], "r")
    # il faut donc rentrer la commande python lexeur.py texte_source.txt
    ch = ""
    L = []
    ch = file.read(1)
    while 1:
        # print(ch)
        if(ch == ""): # fin du fichier
            break
        elif(ch in chiffres):  # pour reconnaitre un nombre
            multi = 1
            nb = [ch]
            while(1):
                ch = file.read(1)
                if(ch in chiffres):
                    multi = multi * 10
                    nb.append(ch)
                else:
                    nombre = 0
                    for i in range(len(nb)):
                        nombre += multi * int(nb[i])
                        multi = multi/10 
                    L.append((int(nombre), "int"))
                    break
        elif(ch == '"'): # pour reconnaitre un string
            word = ""
            while(1):
                ch = file.read(1)
                if(ch == '"'):
                    L.append((word, "mot"))
                    ch = file.read(1)
                    break
                else:
                    word = word + ch
        elif(ch == "/"):  # pour reconnaitre soit la division, soit un commentaire entier, soit un commentaire imbriqué
            ch = file.read(1)
            if(ch == "/"):
                file.readline()
                ch = file.read(1)
            elif(ch == "*"):
                ch = file.read(1)
                while(1):
                    if(ch == "*"):
                        ch = file.read(1)
                        if(ch == "/"):
                            ch = file.read(1)
                            break
                    else:
                        ch = file.read(1)
            else:
                L.append(("/", "operateur"))
                # ch = file.read(1)
        elif(ch in operateur): # pour reconnaitre les opérateurs autres
            L.append((ch, "opérateur"))
            ch = file.read(1)
        elif(ch in symbole): # pour reconnaitre les symboles autres
            L.append((ch, "symbole"))
            ch = file.read(1)
        else:
            ch = file.read(1)
        # print(L)
    file.close()
    return L

L = lexeur()
print(L)
