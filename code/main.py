from lexeur import *
from analyseur_syntaxique import *
def main():
    # fichier = sys.argv[1]
    fichier = "fichier_test_jura/test4.txt"
    L = lexeur(fichier)
    analyseur = Parseur(L)
    var = analyseur.verif_file()
    print(var)




if __name__ == "__main__":
    main()