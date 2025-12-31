from lexeur import *
from erreurs_included import *
def main():
    # fichier = sys.argv[1]
    fichier = "fichier_test_jura/test4.txt"
    L = lexeur(fichier)
    # print(L)
    analyseur = Parseur(L)
    var = analyseur.verif_file()
    print(var)




if __name__ == "__main__":
    main()