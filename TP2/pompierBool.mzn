%les donnes
int: nVille;
array [1..nVille,1..nVille] of int: duree;

%les variables
array [1..nVille] of var 0..1: caserne;
% si casern[i]=1 alors caserne ouverte dans ville v
array [1..nVille,1..nVille] of var 0..1:servi;

include "pompiers.dzn";

%contraintes
% 5 caserne vouverte sert sa ville
constraint forall(i in 1..nVille)(caserne[i] = servi[i,i]);

% 1 toute ville est servie
constraint forall(v in 1..nVille)(sum([servi[i,v]| i in 1..nVille])=1);

% 3 caserne sert une ville a moins de 15min
%constraint forall(c in 1..nVille,v in 1..nVille)(if servi[c,v]=1 then duree[c,v]<=15 endif);
constraint forall(c in 1..nVille,v in 1..nVille)(duree[c,v]*servi[c,v]<=15);

%4 une ville qui sert une autre doit avoir une caserne
constraint forall(c,v in 1..nVille)(servi[c,v]<=caserne[c]);

% 2 minimiser nombre de caserne
solve minimize(sum(caserne));

output ["caserne " ++ " : "++ show(caserne) ++ "\n" ];
output[show(servi[i,j])++ if j==nVille then "\n" else ", " endif | i,j,in 1..nVille];