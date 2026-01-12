from lexeur import lexeur

print("\nlancement des tests")
def test_operation():
    assert(lexeur("./fichier_source_tests/texte_operation.txt") == [(13, 'integer'), ('+', 'opérateurs'), (2, 'integer'), ('=', 'opérateurs'), (26, 'integer'), (13, 'integer'), ('+', 'opérateurs'), (2, 'integer'), ('=', 'opérateurs'), (26, 'integer'), (7, 'integer'), ('/', 'opérateurs'), (3, 'integer'), ('!=', 'opérateurs'), (5, 'integer'), (156987, 'integer')])

def test_operateur():
    assert(lexeur("./fichier_source_tests/texte_operateur.txt") == [('=', 'opérateurs'), ('||', 'opérateurs'), ('&&', 'opérateurs'), ('==', 'opérateurs'), ('!=', 'opérateurs'), ('<', 'opérateurs'), ('<=', 'opérateurs'), ('>', 'opérateurs'), ('>=', 'opérateurs'), ('instanceof', 'opérateurs'), ('+', 'opérateurs'), ('-', 'opérateurs'), ('*', 'opérateurs'), ('/', 'opérateurs'), ('%', 'opérateurs'), ('!', 'opérateurs'), ('cast', 'opérateurs'), ('.', 'opérateurs')])

def test_string():
    assert(lexeur("./fichier_source_tests/texte_string.txt") == [('3 petits chats, 3 petits chats, 3 petits chats, chats, chats', 'mot'), ('il a int sa game de lol', 'mot'), ("c'est pas faux, car ce n'est pas un boolean", 'mot')])

def test_motsclef():
    assert(lexeur("./fichier_source_tests/texte_motsclef.txt") == [('boolean', 'mots clés'), ('class', 'mots clés'), ('else', 'mots clés'), ('extends', 'mots clés'), ('false', 'mots clés'), ('for', 'mots clés'), ('if', 'mots clés'), ('instanceof', 'opérateurs'), ('int', 'mots clés'), ('new', 'mots clés'), ('null', 'mots clés'), ('public', 'mots clés'), ('return', 'mots clés'), ('static', 'mots clés'), ('this', 'mots clés'), ('true', 'mots clés'), ('void', 'mots clés')])

def test_idvsmotclef():
    assert(lexeur("./fichier_source_tests/texte_idvsmotclef.txt") == [('boolean', 'mots clés'), ('bool', 'ident'), ('else_01', 'ident'), ('else', 'mots clés'), ('_instanceof__13', 'ident'), ('test', 'ident')])

def test_symboles():
    assert(lexeur("./fichier_source_tests/texte_symboles.txt") == [('ceci est un paragraphe', 'mot'), ('{', 'symboles'), ('test', 'mot'), ('}', 'symboles'), (';', 'symboles'), ('suivi par des crochets', 'mot'), ('[', 'symboles'), (13, 'integer'), (']', 'symboles'), (';', 'symboles'), ('et enfin des parentheses', 'mot'), ('(', 'symboles'), ('int', 'mots clés'), (')', 'symboles'), (';', 'symboles'), ('et toutes les lignes finissent par un point virgule', 'mot'), (';', 'symboles')])

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
