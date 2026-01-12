from lexeur import lexeur

print("\nlancement des tests")
def test_operation():
    assert(lexeur("./fichier_source_tests/texte_operation.txt") == [(13, 'integer', 1), ('+', 'opérateurs', 1), (2, 'integer', 1), ('=', 'opérateurs', 1), (26, 'integer', 1), (13, 'integer', 2), ('+', 'opérateurs', 2), (2, 'integer', 2), ('=', 'opérateurs', 2), (26, 'integer', 2), (7, 'integer', 3), ('/', 'opérateurs', 3), (3, 'integer', 3), ('!=', 'opérateurs', 3), (5, 'integer', 3), (156987, 'integer', 4)])

def test_operateur():
    assert(lexeur("./fichier_source_tests/texte_operateur.txt") == [('=', 'opérateurs', 1), ('||', 'opérateurs', 2), ('&&', 'opérateurs', 3), ('==', 'opérateurs', 4), ('!=', 'opérateurs', 5), ('<', 'opérateurs', 6), ('<=', 'opérateurs', 7), ('>', 'opérateurs', 8), ('>=', 'opérateurs', 9), ('instanceof', 'opérateurs', 10), ('+', 'opérateurs', 11), ('-', 'opérateurs', 12), ('*', 'opérateurs', 13), ('/', 'opérateurs', 14), ('%', 'opérateurs', 15), ('!', 'opérateurs', 16), ('cast', 'opérateurs', 17), ('.', 'opérateurs', 18)])

def test_string():
    assert(lexeur("./fichier_source_tests/texte_string.txt") == [('3 petits chats, 3 petits chats, 3 petits chats, chats, chats', 'mot', 1), ('il a int sa game de lol', 'mot', 2), ("c'est pas faux, car ce n'est pas un boolean", 'mot', 7)])

def test_motsclef():
    assert(lexeur("./fichier_source_tests/texte_motsclef.txt") == [('boolean', 'mots clés', 1), ('class', 'mots clés', 2), ('else', 'mots clés', 3), ('extends', 'mots clés', 4), ('false', 'mots clés', 5), ('for', 'mots clés', 6), ('if', 'mots clés', 7), ('instanceof', 'opérateurs', 8), ('int', 'mots clés', 9), ('new', 'mots clés', 10), ('null', 'mots clés', 11), ('public', 'mots clés', 12), ('return', 'mots clés', 13), ('static', 'mots clés', 14), ('this', 'mots clés', 15), ('true', 'mots clés', 16), ('void', 'mots clés', 17)])

def test_idvsmotclef():
    assert(lexeur("./fichier_source_tests/texte_idvsmotclef.txt") == [('boolean', 'mots clés', 1), ('bool', 'ident', 1), ('else_01', 'ident', 2), ('else', 'mots clés', 2), ('_instanceof__13', 'ident', 3), ('test', 'ident', 3)])

def test_symboles():
    assert(lexeur("./fichier_source_tests/texte_symboles.txt") == [('ceci est un paragraphe', 'mot', 1), ('{', 'symboles', 1), ('test', 'mot', 1), ('}', 'symboles', 1), (';', 'symboles', 1), ('suivi par des crochets', 'mot', 2), ('[', 'symboles', 2), (13, 'integer', 2), (']', 'symboles', 2), (';', 'symboles', 2), ('et enfin des parentheses', 'mot', 3), ('(', 'symboles', 3), ('int', 'mots clés', 3), (')', 'symboles', 3), (';', 'symboles', 3), ('et toutes les lignes finissent par un point virgule', 'mot', 4), (';', 'symboles', 4)])

def test_erreur():
    assert(lexeur("./fichier_source_tests/texte_erreur.txt") == "Erreur")
           

test_operation()
test_operateur()
test_string()
test_motsclef()
test_idvsmotclef()
test_symboles()
test_erreur()

print("les tests sont passés\n")
