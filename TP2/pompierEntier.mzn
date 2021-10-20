%les donnes
int: nVille;
array [1..nVille,1..nVille] of int: duree;

%les variables
array [1..nVille] of var 0..1: caserne;
% si casern[i]=1 alors caserne ouverte dans ville v
array [1..nVille] of var 1..nVille:ass;

include "pompiers.dzn";

%contraintes
% 5 caserne ouverte sert sa ville
constraint forall(i in 1..nVille)(caserne[i]=1 -> ass[i]=i);

% 1 toute ville est servie
%déjà assuré par le domaine

% 3 caserne sert une ville a moins de 15min
constraint forall(v in 1..nVille)(duree[v,ass[v]]<=15);

%4 une ville qui sert une autre doit avoir une caserne
constraint forall(v in 1..nVille)(caserne[ass[v]]=1);

%ou
%constraint forall(v in 1..nVille)(duree[v,ass[v]]<=15
%                                  /\
%                                  caserne[ass[v]]=1
%);

% 2 minimiser nombre de caserne
solve minimize(sum(caserne));

output ["caserne " ++ " : "++ show(caserne) ++ "\n" ];
output[show(ass)];