int: nc;
int: nr;
array [1..nr,1..nr] of 0..1: graphe;
array [1..nr] of var 1..nc: couleur;

include "coloration-gr.dzn";

constraint forall(i,j in 1..nr where i<j /\ graphe[i,j]!=0)(
     couleur[i]!=couleur[j]
     );
     
%ou bien 
% constraint forall (i,j in 1..nr where i<j)(if graphe[i,j]!=0 then couleur[i]!=couleur[j] endif);
solve satisfy;