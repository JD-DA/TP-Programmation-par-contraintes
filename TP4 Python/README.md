#Projet Facultatif : Solveur PPC
####Jean-Daniel de Ambrogi 2183171

###Ajouts

- Heuristiques de choix de variables dynamiques : choix par nombre de support, cardinalité du domaine restant, en fonction du nombre de la proximité du nombre de support au nombre de support médian, proximité du nombre de support au nombre de support moyen. Ordre croissant et décroissant.
- Contraintes binaires : = , != , < , > , <= , >= 
- Propagation de contraintes : AC4


###Détails :
####Heuristiques
- Nombre de support : Ajout de l'ordre croissant et décroissant sur le nombre de support pour les valeurs du domaine de la variable. Implémentation d'une fonction ```getNumSupport``` dans les contraintes.
- Cardinalité du domaine restant : ordre croissant et décroissant
- Médiane : Supposition sur le fonctionnement. On ordonne les variables en fonction de leur proximité avec le nombre de support médian. Ainsi dans l'ordre croissant on retrouve les variables tel que |nb-Support - nbSupportMedian| est le plus petit en premier.
- Moyenne : même fonctionnement que pour la médiane
###Contraintes binaires
- Seule difficultée rencontrée : pour ```unsat``` on cherche a savoir si le domaine permet de satisfaire la contrainte or pour l'égalité on doit parcourir toutes les valeurs pour trouver si l'égalité est possible. Au départ je suis parti sur test plus générale qui vérifiait si il était *possible* de satisfaire la contrainte sans assurance juste en testant le min et le max. Après quelques tests je me suis vite rendu compte que cela ne pouvait fonctionner.
###AC4
J'ai implémenté AC4 en suivant l'algorithme du cours. Pour le tester j'ai repris l'exemple de celui-ci : testCP4.py
On retrouve bien les même valeurs dans Q, counter et S.



