from solver import Solver
from csp import  CSP
from constraint import *
from typing import Dict, List, Optional

if __name__ == "__main__":
    variables: List[str] = ["x", "y","z"]
    domains: Dict[str, List[int]] = {}
    for var in variables:
        domains[var] = [1, 2, 3]
    csp = CSP(variables, domains)
    csp.add_constraint(Different("x", "y"))
    csp.add_constraint(Superieur("x", "z"))
    #csp.add_constraint(Table(["y", "z"],((2,2),(1,2))))
    #csp.add_constraint(Egalite("y","z"))

    solver = Solver()
    #solver.backtracking_search(csp)
    #solver.bt_forward(csp)
    #solver.propagate_AC1(csp)
    #print(csp.domains)
    solver.bt_propagation(csp,solver.propagate_AC3)
    print("Number of nodes: ",solver.nbNodes)
        
