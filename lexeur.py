chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alpha_min = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alpha_maj = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def lexeur(txt):
    f = open(txt,'r')
    c = f.read(1)
    L = []
    print("après", c)
    while c != "":
        if c in chiffres:
            L.append(("int", int(c)))
            c = f.read(1)
        elif c in alpha_min or c in alpha_maj: #IL FAUDRA RAJOUTER LES VARIABLES -> VA FAIRE BCP DE IF :(((
            # A VERIFIER -> tests
            if c == "b":
                c = f.read(1)
                if c == "o":
                    L.append("mots clés", "boolean")
                    f.read(6)
                else:
                    L.append("alpha", "b")
            elif c == "c":
                c = f.read(1)
                if c == "l":
                    L.append(("mots clés", "class"))
                    f.read(4)
                else:
                    L.append(("alpha","c"))
            elif c == "e":
                c = f.read(1)
                if c == "l":
                    L.append(("mots clés", "else"))
                    f.read(3)
                elif c == "x":
                    L.append(("mots clés", "extends"))
                    f.read(6)
                else:
                    L.append(("alpha", "c"))
            elif c == "f":
                c = f.read(1)
                if c == "a":
                    L.append(("mots clés", "false"))
                    f.read(4)
                elif c == "o":
                    L.append(("mmots clés"), "for")
                    f.read(2)
                else:
                    L.append(("alpha", "f"))
            elif c == "i":
                c = f.read(1)
                if c == "f":
                    L.append(("mots clés", "if"))
                    f.read(1)
                elif c == "n":
                    c = f.read(1)
                    if c == "s":
                        L.append(("mots clés", "instanceof"))
                        f.read(9)
                    elif c == "t":
                        L.append(("mots clés", "int"))
                        f.read(1)
                    else:
                        L.append(("ident", "in")) #IL NE DEVRAIT PAS ENCORE Y AVOIR DE INDENT, MAIS PAS LE CHOIX
                else:
                    L.append(("alpha", "i"))
            #ON CONTINUE à N -> NEW NULL


            
            L.append(("alpha", c))
            c = f.read(1)
        elif c == '"' or c == ";" or c == "{" or c == "}" or c == "(" or c == ")" or c == "[" or c == "]":
            L.append(("symboles", c))
            c = f.read(1)
        elif c == "|":
            c = f.read(1)
            if c != "|":
                return
            else:
                L.append(("opérateurs", "||"))
                c = f.read(1)
        elif c == "&":
            c = f.read(1)
            if c != "&":
                return
            else:
                L.append(("opérateurs", "&&"))
                c = f.read(1)
        elif c == "+" or c == "*" or c == "%":
            L.append(("opérateurs", c))
            c = f.read(1)
    f.close()
    return(L)







if __name__ == "__main__":
    L = lexeur("miaou.txt")
    print(L)