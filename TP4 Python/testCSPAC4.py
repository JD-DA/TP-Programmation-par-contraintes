from solver import Solver
from csp import  CSP
from constraint import *
from typing import Dict, List, Optional

if __name__ == "__main__":
    variables: List[str] = ["x1", "x2","x3"]
    domains: Dict[str, List[int]] = {}
    for var in variables[:-1]:
        domains[var] = [1, 2, 3,4]
    domains["x3"] = [3]
    csp = CSP(variables, domains)
    csp.add_constraint(InferieurOuEgal("x1", "x2"))
    csp.add_constraint(Different("x2", "x3"))

    solver = Solver()
    solver.bt_propagation(csp,solver.propagate_AC3)
    print("Number of nodes: ",solver.nbNodes)
        
