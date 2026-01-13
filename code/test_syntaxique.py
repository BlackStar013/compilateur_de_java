from lexeur import *
from erreurs_included import *
from nodes_class import *
from dessiner import *
print("\nlancement des tests")


def test_class_Main():
    fichier = "./fichier_test_jura/test1.txt"
    parseur = Parseur(lexeur(fichier))
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(parseur.nb_erreurs == 0)
    assert isinstance(verif, File)

    viz = initialisation(verif)
    show(verif, "arbre_test_final")


def test_class_mainetMain():
    fichier = "./fichier_test_jura/test2.txt"
    parseur = Parseur(lexeur(fichier))
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(parseur.nb_erreurs == 0)
    assert isinstance(verif, File)

def test_erreur():
    fichier = "./fichier_test_jura/test3.txt"
    parseur = Parseur(lexeur(fichier))
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(parseur.nb_erreurs > 0)


def test_POO():
    fichier = "./fichier_test_jura/test4.txt" #test de this + parenthèses + if + commentaires + plus fonctions avant main...
    lex = lexeur(fichier)
    parseur = Parseur(lex)
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(parseur.nb_erreurs == 0)


def test_plusieurs_class_avant_Main():
    fichier = "./fichier_test_jura/test5.txt"
    lex = lexeur(fichier)
    parseur = Parseur(lex)
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(parseur.nb_erreurs == 0)

def test_operations():
    fichier = "./fichier_test_jura/test6.txt"
    lex = lexeur(fichier)
    parseur = Parseur(lex)
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(parseur.nb_erreurs == 0)


def test_accolade():
    fichier = "./fichier_test_jura/test7.txt"
    lex = lexeur(fichier)
    parseur = Parseur(lex)
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(parseur.nb_erreurs == 0)



def test_egal():
    fichier = "./fichier_test_jura/test8.txt"
    lex = lexeur(fichier)
    parseur = Parseur(lex)
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(parseur.nb_erreurs > 0)



def test_crochet():
    fichier = "./fichier_test_jura/test9.txt"
    lex = lexeur(fichier)
    parseur = Parseur(lex)
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(parseur.nb_erreurs > 0)


def test_parenthese_if():
    fichier = "./fichier_test_jura/test10.txt"
    lex = lexeur(fichier)
    parseur = Parseur(lex)
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(parseur.nb_erreurs > 0)


def test_addition():
    fichier = "./fichier_test_jura/test11.txt"
    lex = lexeur(fichier)
    parseur = Parseur(lex)
    # print(parseur.tokens)
    verif = parseur.verif_file()
    assert(parseur.nb_erreurs > 0)


if __name__ == "__main__":
    test_class_Main() #1
    test_class_mainetMain() #2
    test_erreur() #3
    test_POO() #4
    test_plusieurs_class_avant_Main() #5
    test_operations() #6
    test_accolade()#7
    test_egal()#8
    test_crochet()#9
    test_parenthese_if()#10
    # test_addition()#11
    print("les tests sont passés\n")