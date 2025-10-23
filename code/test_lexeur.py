from lexeur import lexeur

print("\nlancement des tests")
def test_nombre():
    assert(lexeur("./code/texte_source.txt") == [(13, 'int'), ('+', 'opérateur'), (2, 'int'), ('=', 'opérateur'), ('ChAt_13', 'mot'), ('miaou', 'mot'), (';', 'symbole'), (',', 'symbole'), ('{', 'symbole'), ('}', 'symbole'), ('(', 'symbole'), (')', 'symbole'), ('[', 'symbole'), (']', 'symbole')])

test_nombre()
print("les tests sont passés\n")