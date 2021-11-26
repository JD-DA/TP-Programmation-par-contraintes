# definition d'un CSP

from typing import Generic, TypeVar, Dict, List, Optional
from constraint import Constraint, Var, Value


# Un CSP est définit par une liste de variables chacune avec son domaine
# et un ensemble de contraintes
class CSP:
    def __init__(self, variables: List[Var], domains: Dict[Var, List[Value]]):
        # les variables du CSP
        self.variables: List[Var] = variables
        # les domaines
        self.domains: Dict[Var, List[Value]] = domains
        # la liste qui contiendra les contraintes qui sont à ajouter
        self.ctrList: List[Constraint[Var, Value]] = []
        self.vcList: Dict[Var, List[Constraint[Var, Value]]] = {}
        for var in self.variables:
            self.vcList[var] = []
            if var not in self.domains:
                raise LookupError("Chaque variable doit avoir son domaine")

    def add_constraint(self, constraint):
        self.ctrList.append(constraint)
        for var in constraint.variables:
            if var not in self.variables:
                raise LookupError("Variable n'est pas du CSP")
            else:
                self.vcList[var].append(constraint)

    # vérifier si une affectation d'une variable n'a pas de conflit avec le CSP
    def consistent(self, var: Var) -> bool:
        for constraint in self.vcList[var]:
            if constraint.unsat(self.domains):
                return False
        return True

    # vérifier si tous les domaines sont singletons
    def singleton(self) -> bool:
        for var in self.variables:
            if len(self.domains[var]) > 1:
                return False
        return True

    # vérifier si le CSP est satisfait avec les domaines actuels
    def satisfied(self) -> bool:
        for constr in self.ctrList:
            if constr.unsat(self.domains):
                return False
        return True

    # créer une solution sous forme de dictionnaire
    def solution(self) -> Dict[Var, Value]:
        sol: Dict[Var, Value] = {}
        for var in self.variables:
            sol[var] = self.domains[var][0]
        return sol

    # retourner une variable non affectée
    def unassignedVar(self) -> Var:
        for var in self.variables:
            if len(self.domains[var]) > 1:
                return var
        return None

    # heuristique qui trie les variable dans l'ordre inverse de leur degré
    def heuristique_tri(self) -> Var:
        self.variables.sort(key=(lambda x: len(self.domains[x])), reverse=True)
        return None

    def getNombreSupport(self, var) -> int:
        num = 0
        for constr in self.ctrList:
            i, j = constr.variables[0], constr.variables[1]
            if i == var or j == var:
                num += constr.getNumSupport(var, self.domains)
        print("For "+var+" : "+str(num))
        return num

    # retourner une variable non affectée
    def unassigned_var_spec(self, heuristic) -> Var:
        if heuristic == "croissantDegréDyn":  # ordonne dans l'ordre décroissant des degrés à chaque appel
            self.variables.sort(key=(lambda x: len(self.domains[x])))
        elif (heuristic == "decroissantSupport"):
            self.variables.sort(key=(lambda x: self.getNombreSupport(x)), reverse=True)
        elif (heuristic == "croissantSupport"):
            self.variables.sort(key=(lambda x: self.getNombreSupport(x)), reverse=False)
        print(self.variables)
        for var in self.variables:
            if len(self.domains[var]) > 1:
                return var
        return None

    # créer une copie des domaines
    def domainsCopy(self):
        d_copy = self.domains.copy()
        for var in self.variables:
            d_copy[var] = self.domains[var].copy()
        return d_copy

    # vérifier si un des domaine est vide
    def emptyDomain(self):
        for var in self.variables:
            if self.domains[var] == []:
                return True
        return False
