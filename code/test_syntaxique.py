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


def test_plusieurs_class_avant_Main():
    fichier = "./fichier_test_jura/test5.txt"
    parseur = Parseur(lexeur(fichier))
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(verif == True)

def test_operations():
    fichier = "./fichier_test_jura/test6.txt"
    lex = lexeur(fichier)
    parseur = Parseur(lex)
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(verif == True)

if __name__ == "__main__":
    test_class_Main() #1
    test_class_mainetMain() #2
    test_erreur() #3
    test_plusieurs_class_avant_Main() #5
    test_operations() #6
    print("les tests sont passés\n")