# PCL1
Ce projet implémente un analyseur lexical et syntaxique pour le langage Jura. Il utilise une approche d'analyse descendante récursive manuelle et génère un Arbre Syntaxique Abstrait (AST).

## Prérequis
Installer les dépendances:
```bash
pip install -r requirements.txt
```

Le logiciel Graphviz installé sur votre machine pour le rendu des images. Visitez graphviz.org pour avoir le guide d'installation.

## Utilisation

Pour lancer la compilation d'un fichier source et visualiser son arbre syntaxique, vous pouvez utiliser un script Python (par exemple `main.py`) contenant les instructions suivantes :

```python
from lexeur import *
from erreurs_included import *
from dessiner import *

# 1. Spécifiez le chemin vers votre fichier source Jura
fichier = "./fichier_test_jura/test3.txt"

# 2. Lancement de la chaîne de compilation
# Etape A : Analyse Lexicale (Fichier -> Liste de Tokens)
tokens = lexeur(fichier)

# Etape B : Analyse Syntaxique (Tokens -> Arbre AST)
parseur = Parseur(tokens)
verif = parseur.verif_file()

# 3. Visualisation graphique
# Génère l'objet Graphviz à partir de la racine de l'AST
viz = initialisation(verif)

# Sauvegarde et ouvre le fichier PDF (ex: "arbre_test3.pdf")
show(viz, "arbre_test3")
```

## Structure du Projet

L'architecture du compilateur est répartie sur plusieurs modules Python, chacun ayant une responsabilité unique :

| Fichier / Dossier | Description |
| :--- | :--- |
| **`lexeur.py`** | **Analyseur Lexical.** Lit le fichier source et convertit le flux de caractères en une liste de tokens (mots-clés, identifiants, opérateurs) |
| **`erreurs_included.py`** | **Analyseur Syntaxique (Parseur).** Il contient la logique d'analyse descendante récursive (méthodes `verif_expr`, `verif_stmt`, etc.) et la gestion des erreurs de syntaxe. |
| **`nodes_class.py`** | **Définition de l'AST.** Définit les classes représentant les nœuds de l'AST (`Node`, `StmtIf`, `OpBin`, `File`, etc.) |
| **`dessiner.py`** | **Visualisation.** Module parcourant récursivement l'AST généré pour construire un graphe visuel à l'aide de la librairie **Graphviz**. |
