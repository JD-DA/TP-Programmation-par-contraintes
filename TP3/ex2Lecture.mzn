include "globals.mzn";
%les donnees
include "lecture.mzn";

%les variables
array [1..N] of var 1..M: affectP;
% affectP[i] = le n° de groupe de la personne i
array [1..M] of var set of 1..K: groupeL;
% groupL[i] = l'ensemble des livres associés au groupe i
array[1..N] of var 0..K : satP;
% satP[i] = Score de satisfaction de la personne i

%satisfactions minimale
var 1..K: minSat;
%somme des satisfactions
var 0..M*K : sumSat;
%c1 un livre est associée a un et un seul groupe
constraint (array_union(groupeL)={i|i in 1..K} /\ all_disjoint(groupeL));

%c2 une personne est associée a un groupe
%domaine

%c3 Les groupes doivent etre équilibré en nb de personnes
% soit affectP[j]=i <=> personne j est associée au groupe i, 
% donc le nombre de fois que i apparait <=> au nombre de personnes 
% dans le groupe i, d'où count(i,affectP) => compter le nombre 
% de i dans affectP 
constraint forall(i in 1..M)(N div M-1 <= count(affectP,i) /\ count(affectP,i)<= ceil(N/M)+1);
%ou bien (plus efficace)
%constraint global_cardinality_low_up(affectP,[i|i in 1..M],[N div M-1| i in 1..M], [ceil(N/M)+1|i in 1..M]);

%c4 les groupes doivent etre équilibres en terme de nombre 
% de livres
constraint forall(i in 1..M)(K div M-1 <= card(groupeL[i]) /\ card(groupeL[i])<= ceil(K/M)+1);

%c5 le score de satisfaction d'une personne est égale au nombre de livres 
% qui l'intéresse associées a son groupe
constraint forall(i in 1..N) (card(preferences[i] intersect groupeL[affectP[i]]) = satP[i]);

%c6 le score global est a somme des score de satisfaction
constraint minSat= min(satP);
constraint sumSat= sum(satP);

%solve maximize(sumSat);
%solve maximize(minSat);
solve maximize(N*minSat+sumSat);

output[show(affectP)];
output[show(groupeL)];
output[show(satP)];
