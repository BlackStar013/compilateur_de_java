from lexeur import *
from analyseur_syntaxique import *
print("\nlancement des tests")


def test_class_Main():
    fichier = "./fichier_test_jura/test1.txt"
    parseur = Parseur(lexeur(fichier))
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(verif == True)

def test_class_mainetMain():
    fichier = "./fichier_test_jura/test2.txt"
    parseur = Parseur(lexeur(fichier))
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(verif == True)

def test_erreur():
    fichier = "./fichier_test_jura/test3.txt"
    parseur = Parseur(lexeur(fichier))
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(verif == False)


print("les tests sont passés\n")
