int: N=10;
int: M=3;
int: K=8;

int: Art=1; int: BD=2; int: Litterature=3; int: Loisirs=4; int: Nature=5; int: Policier=6; int: Politique=7; int: SF=8;

array [1..N] of string: nomPers=["pierre", "jean", "paul", "julien", "ahmed", "marie", "isabelle", "sylvie", "alice", "carole"];

array [1..N] of set of int: preferences=
  [ {2, 8, 4},  {6, 7, 8},  {3, 1},  {4, 5, 2},  {5, 1, 4}, 
    {2, 6, 7},  {3, 7, 4},  {3, 7, 1},  {7, 1, 5},  {4, 5, 1} ];
    
    