int: NPERS;
int: NTABLES;
int: NMETS;
int: CAPACITE;

include "picnic.dzn";
include "globals.mzn";


array [1..NPERS] of var 1..NTABLES: placerPer; %placerPer[i] le num de table de la personne i
array [1..NTABLES] of var set of 1..NMETS: metsTable; %metsTable[i] l'ensemble des mets de la table i
array [1..NPERS, 1..NTABLES] of var set of 1..NMETS: app; %app[i,j] l'ensemble des mets que la personne i apporte sur la table j

%c1 capacite des tables 
constraint forall(i in 1..NPERS)(count(placerPer,i) <=CAPACITE);


%c2
constraint forall(i in 1..NPERS, j in 1..NTABLES)(app[i,j] = (if placerPer[i]=j then APPORTE[i] else {} endif));
%remplir metsTable
constraint forall(j in 1..NTABLES)(metsTable[j]=array_union(i in 1..NPERS)(app[i,j]));

constraint forall(i in 1..NTABLES)(metsTable[i] intersect ENTREES != {});
constraint forall(i in 1..NTABLES)(metsTable[i] intersect PLATS != {});
constraint forall(i in 1..NTABLES)(metsTable[i] intersect DESSERTS != {});

constraint forall(i in 1..NPERS)((metsTable[placerPer[i]] diff DETESTE[i]) intersect ENTREES != {});
constraint forall(i in 1..NPERS)((metsTable[placerPer[i]] diff DETESTE[i]) intersect PLATS != {});
constraint forall(i in 1..NPERS)((metsTable[placerPer[i]] diff DETESTE[i]) intersect DESSERTS != {});

constraint placerPer[1]=1;

solve satisfy;

