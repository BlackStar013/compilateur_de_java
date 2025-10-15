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
        elif c in alpha_min or c in alpha_maj:
            L.append(("alpha", c))
        elif c == '"' or c == ";" or c == "{" or c == "}" or c == "(" or c == ")" or c == "[" or c == "]":
            L.append(("symboles", c))
        elif c == "|":
            c = f.read(1)
            if c != "|":
                return
            else:
                L.append(("opérateurs", "||"))
        elif c == "&":
            c = f.read(1)
            if c != "&":
                return
            else:
                L.append(("opérateurs", "&&"))
        elif c == "+" or c == "*" or c == "%":
            L.append(("opérateurs", c))
        c = f.read(1)
    f.close()
    return(L)







if __name__ == "__main__":
    L = lexeur("miaou.txt")
    print(L)