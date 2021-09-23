include "globals.mzn";
var 1..9: S;
var 0..9: N;
var 0..9: D;
var 1..9: M;
var 0..9: E;
var 0..9: O;
var 0..9: R;
var 0..9: Y;
%peu efficace car l'autre a une contrainte globale qui permet une meilleurs recherche: plus puissant
var 0..1: R1;
var 0..1: R2;
var 0..1: R3;


constraint S!=0;
constraint M!=0;
constraint all_diferetn([S,E,N,D,M,O,R,Y]);
constraint D+E = 10*R1+Y;
constraint R1+R+N = 10*R2+E;
constraint R2+E+O = 10*R3+N;
constraint R3+S+M = 10*M+O;

solve satisfy;


output ["  \(S)\(E)\(N)\(D)\n",
        "+ \(M)\(O)\(S)\(T)\n",
         "=\(M)\(O)\(N)\(E)\(Y)",  "\n"];