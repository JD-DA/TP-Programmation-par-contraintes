from abc import ABC, abstractmethod
from typing import Dict, List, Optional

#Var = TypeVar('Var') # type pour variable
Var = 'str'
#Value = TypeVar('Value') # type pour domaine
Value = 'int'

# classe pour les contraintes
class Constraint(ABC):
    # constructeur initie les variables
    def __init__(self, variables: List[Var]) -> None:
        self.variables = variables

    # fonctions à redéfinir pour chaque contrainte
    # tester si les domaines sont en conflit la contrainte
    @abstractmethod
    def unsat(self, domains: Dict[Var, List[Value]]) -> bool:
        ...

    # tester si la valeur "value" de la variable "var" a un support
    @abstractmethod
    def checkSupport(self, var: Var, value: Value, domains: Dict[Var, List[Value]]) -> bool:
        ...
        
    # enlever les valeurs sans support de la variable "revisedVar"
    # retourner True si ces valeurs existent
    def propagate(self, revisedVar, domains: Dict[Var, List[Value]]) -> bool:
        listRem = []
        for val in domains[revisedVar]:
            if self.checkSupport(revisedVar, val, domains) == False:
                listRem.append(val)
        for val in listRem:
            domains[revisedVar].remove(val)
        if len(listRem)==0:
            return False
        return True
    
class Different(Constraint):
    def __init__(self, v1, v2) -> None:
        super().__init__([v1, v2])
        self.v1 = v1
        self.v2 = v2

    def unsat(self, domains: Dict[str, List[int]]) -> bool:
        cardV1 = len(domains[self.v1])
        cardV2 = len(domains[self.v2])
        if(cardV2>1 or cardV1>1):   #si un des domaines a une cardinalitée supérieure à 1 alors c'est satisfiable
            return False
        return (cardV2==0 or cardV2==0) or domains[self.v1][0]==domains[self.v2][0]


    def checkSupport(self, var, value, domains) -> bool:
        if var==self.v1:
            varTest = self.v2
        else:
            varTest = self.v1
        for valueTest in domains[varTest]:
            if(value != valueTest):
                return True
        return False

class Egalite(Constraint):
    def __init__(self, v1, v2) -> None:
        super().__init__([v1, v2])
        self.v1 = v1
        self.v2 = v2

    def unsat(self, domains: Dict[str, List[int]]) -> bool:
        return not (
        (max(domains[self.v1]) >= min(domains[self.v2]) and min(domains[self.v1]) <= min(domains[self.v2])) or (max(domains[self.v2]) >= min(domains[self.v1]) and max(domains[self.v2]) <= max(domains[self.v1])))  # le plus grand élément de v1 est sup ou plus petit de v2

    def checkSupport(self, var, value, domains) -> bool:
        if var==self.v1:
            varTest = self.v2
        else:
            varTest = self.v1
        for valueTest in domains[varTest]:
            if(value == valueTest):
                return True
        return False

    ##contraintes binaires, ac3, heuristiques
class Superieur(Constraint):
    def __init__(self, v1: str, v2: str):
        super().__init__([v1,v2])
        self.v1 = v1
        self.v2 = v2
    
    def unsat(self, domains: Dict[str, List[int]]) -> bool:
        return not((max(domains[self.v1])>min(domains[self.v2]))) #le plus grand élément de v1 est sup ou plus petit de v2
    
    def checkSupport(self, var, value, domains) -> bool:
        if var==self.v1:
            return value>min(domains[self.v2])
        else:
            return value<max(domains[self.v1])


class SuperieurOuEgal(Constraint):
    def __init__(self, v1: str, v2: str):
        super().__init__([v1, v2])
        self.v1 = v1
        self.v2 = v2

    def unsat(self, domains: Dict[str, List[int]]) -> bool:
        return not (
        (max(domains[self.v1]) >= min(domains[self.v2])))  # test si le plus grand élément de v1 est >= au plus petit de v2

    def checkSupport(self, var, value, domains) -> bool:
        if var == self.v1:
            return value >= min(domains[self.v2])
        else:
            return value <= max(domains[self.v1])
class Inferieur(Constraint):
    def __init__(self, v1: str, v2: str):
        super().__init__([v1, v2])
        self.v1 = v1
        self.v2 = v2

    def unsat(self, domains: Dict[str, List[int]]) -> bool:
        return not (
        (max(domains[self.v1]) < min(domains[self.v2])))  # test si le plus grand élément de v1 est >= au plus petit de v2

    def checkSupport(self, var, value, domains) -> bool:
        if var == self.v1:
            return value < min(domains[self.v2])
        else:
            return value > max(domains[self.v1])

class InferieurOuEgal(Constraint):
    def __init__(self, v1: str, v2: str):
        super().__init__([v1, v2])
        self.v1 = v1
        self.v2 = v2

    def unsat(self, domains: Dict[str, List[int]]) -> bool:
        return not (
        (max(domains[self.v1]) >= min(domains[self.v2])))  # test si le plus grand élément de v1 est >= au plus petit de v2

    def checkSupport(self, var, value, domains) -> bool:
        if var == self.v1:
            return value >= min(domains[self.v2])
        else:
            return value <= max(domains[self.v1])

class Table(Constraint):
    def __init__(self, varList, tupleTable):
        super().__init__(varList)
        self.table = tupleTable
        
    def unsat(self, domains: Dict[str, List[int]]) -> bool:
        for (i,j) in self.table:
            if i in domains[self.variables[0]] and  j in domains[self.variables[1]]:
                return False
        return True
    
    def checkSupport(self, var, value, domains) -> bool:
        if var==self.variables[0]:
            indice = 0
            varTest = self.variables[1]
        else:
            indice = 1
            varTest = self.variables[0]
        for (i,j) in self.table :
            if([i,j][indice]==value):
                return True
        return False



