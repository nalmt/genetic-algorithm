# genetic-algorithm

Emna Barred & Nabil LAMRABET

# Codage du génotype

Le génotype est une suite de caractères [A-Z] [0-9]

La proximité des caractères est la suivante :

Pour les lettres, la proximité est l'ordre alphabétique, A et B ont une proximité de 1.

Pour les chiffres, la proximité est l'ordre numérique, 0 et 1 ont une proximité de 1.

La lettre Z a une proximité de 1 avec le chiffre 0, 

le chiffre 9 a une proximité de 1 avec la lettre A.

On peut représenter la proximité de cette façon :

```
A-B-C-D-E-F-G-H-I-K-L-M-N-OP-Q-R-S-T--U-V-W-X-Y-Z-0-1-2-3-4-5-6-7-8-9
```

Avec 9 qui boucle sur A, ou :

```
0-1-2-3-4-5-6-7-8-9-A-B-C-D-E-F-G-H-I-K-L-M-N-OP-Q-R-S-T--U-V-W-X-Y-Z
```

Avec Z qui boucle sur 0.

# Sélection

On sélectionne deux individus avec la "roulette-wheel" sélection.

La part d'un individu dans la roulette est proportionnelle à sa fitness.

Ici, la fitness est calculée avec la proximité de l'individu par rapport au mot de passe de l'utilisateur.

On ajoute  à la nouvelle population une version mutée de chacun et un cross-over des deux avec une certaine probabilité.

On réitère ces manipulations jusqu'à avoir une population de taille (population précédente - 2).

On ajoute ensuite les deux individus de la population précédente ayant les meilleurs fitness.

# Mutation

On parcourt chaque gène d'un individu, le gène a une probabilité de muter (pour l'instant on la fixe à 0.2).

Ensuite on a une probabilité de supprimer un gène au hasard et une probabilité d'ajouter un gène au hasard (ces types de mutations s'appliquent uniquement si nous avons 13 à 17 gènes inclus).

# Cross-over

On ajoute avec une probabilité un cross-over des deux individus sélectionnés.

On peut échanger un certain fixes de gènes, ces gènes choisis au hasard (exemple on échange les gènes de rang 4, 5, 8, 9, 10).

On peut échanger les gènes à partir d'un certain rang fixé (exemple : on échange tous les gènes de rang supérieur à 5).

# Hyper-paramètres

À définir en essayant.