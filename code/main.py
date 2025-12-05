from lexeur import *
from analyseur_syntaxique import *  

def main():
    fichier = sys.argv[1]
    L = lexeur(fichier)
    analyseur = Parseur(L)
    var = analyseur.verif_file()
    print(var)




if __name__ == "__main__":
    main()