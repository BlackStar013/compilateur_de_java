<<<<<<< HEAD
from graphviz import *
from nodes_class import *

def initialisation(racine):
    arbre = Digraph(comment='AST')
    arbre.attr('node', shape='box', style='filled', fontname='Arial')

    if racine is not None:
        ajout_arete(arbre, racine)
    
    return arbre

def ajout_arete(arbre:Digraph, node:Node):
    #ID unique pour chaque noeud
    node_id = str(id(node))

    #étiquette du noeud
    label = f"<{node.type}>"
    
    arbre.node(name=node_id, label=label)

    #parcours des fils
    if node.fils:
        for f in node.fils:
            if f is not None:
                ajout_arete(arbre, f)
                arbre.edge(node_id, str(id(f)))
            else: #nécessaire ?
                none_id = f"None"
                arbre.node(none_id, shape='point', width='0.1')
                arbre.edge(node_id, none_id)
            

def show(arbre:Digraph, filename:str):
    arbre.render(filename, view=True, format='png')

# Test de construction
if __name__ == "__main__":
    # 1. Création des instructions du corps de la méthode
    # x = 1;
    assign = Attribution(Ident("x"), Element("integer", 1))
    stmt_assign = ExprStmt(assign)
    
    # Bloc d'instructions
    corps_methode = Stmtes([stmt_assign])

    # 2. Création de la méthode test()
    methode = Methode("test", "void", [], [corps_methode])

    # 3. Création du champ 'int x'
    champ = Champ("int", "x")

    # 4. Création de la classe A
    classe_A = Class("A", None, [champ, methode])

    # 5. Main Class (vide pour l'exemple)
    main = Class_Main("Main", "args", [])

    # 6. Fichier complet
    fichier = File(main, [classe_A])

    # --- Visualisation ---
    viz = initialisation(fichier)
    show(fichier, "arbre_test_final")
=======
from graphviz import *
from nodes_class import *

def initialisation(racine):
    arbre = Digraph(comment='AST')
    arbre.attr('node', shape='box', style='filled', fontname='Arial')

    if racine is not None:
        ajout_arete(arbre, racine)
    
    return arbre

def ajout_arete(arbre:Digraph, node:Node):
    #ID unique pour chaque noeud
    node_id = str(id(node))

    #étiquette du noeud
    label = f"<{node.type}>"
    
    arbre.node(name=node_id, label=label)

    #parcours des fils
    if node.fils:
        for f in node.fils:
            if f is not None:
                ajout_arete(arbre, f)
                arbre.edge(node_id, str(id(f)))
            else: #nécessaire ?
                none_id = f"None"
                arbre.node(none_id, shape='point', width='0.1')
                arbre.edge(node_id, none_id)
            

def show(arbre:Digraph, filename:str):
    arbre.render(filename, view=True, format='png')
>>>>>>> Loan
