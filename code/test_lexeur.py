from lexeur import lexeur

print("\nlancement des tests")
def test_nombre():
    assert(lexeur("texte_source.txt") == [(13, 'int'), ('+', 'opérateur'), (2, 'int'), ('=', 'opérateur'), ('ChAt_13', 'mot'), ('miaou', 'mot'), (';', 'symbole'), (',', 'symbole'), ('{', 'symbole'), ('}', 'symbole'), ('(', 'symbole'), (')', 'symbole'), ('[', 'symbole'), (']', 'symbole')])

print("les tests sont passés\n")